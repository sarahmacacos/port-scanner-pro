import socket
from services import identify_service


def scan_port(ip, port, timeout):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((ip, port))
        sock.close()
        return True
    except:
        return False


def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip, port))
        banner = sock.recv(1024).decode(errors="ignore").strip()
        sock.close()
        return banner
    except:
        return None


def analyze_port(ip, port, timeout):
    if scan_port(ip, port, timeout):
        service = identify_service(port)
        banner = grab_banner(ip, port)

        return {
            "port": port,
            "service": service,
            "banner": banner
        }

    return None