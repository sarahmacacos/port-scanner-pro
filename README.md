# Python Port Scanner Pro

Multithreaded TCP port scanner built in Python for network reconnaissance and basic service fingerprinting.

---

## Overview

This project simulates a real-world cybersecurity tool used during the reconnaissance phase.

It scans a target host across a specified port range, identifies open ports, performs banner grabbing, and maps common services.

---

## Features

* TCP port scanning using sockets
* Multithreading for fast execution
* Service identification
* Banner grabbing
* CLI interface with argparse
* JSON output

---

## Usage

```bash
python main.py -t scanme.nmap.org -p 1-1000
```

---

## Example Output

```
[+] 22 OPEN | SSH
[+] 80 OPEN | HTTP
```

---

## Disclaimer

For educational purposes only.
