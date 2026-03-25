import argparse
import threading
import time
from queue import Queue
from scanner import analyze_port
from output import save_results

queue = Queue()
results = []

def worker(ip, timeout):
    while not queue.empty():
        port = queue.get()

        result = analyze_port(ip, port, timeout)

        if result:
            print(f"[+] {result['port']} OPEN | {result['service']}")
            results.append(result)

        queue.task_done()


def run_scan(ip, start_port, end_port, threads, timeout):
    start_time = time.time()

    for port in range(start_port, end_port + 1):
        queue.put(port)

    for _ in range(threads):
        t = threading.Thread(target=worker, args=(ip, timeout))
        t.start()

    queue.join()

    duration = time.time() - start_time

    print("\n📊 Scan finalizado")
    print(f"Tempo: {duration:.2f}s")
    print(f"Portas abertas: {len(results)}")

    save_results(results)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--target", required=True)
    parser.add_argument("-p", "--ports", required=True)

    args = parser.parse_args()

    start, end = map(int, args.ports.split("-"))

    run_scan(args.target, start, end, 50, 1)