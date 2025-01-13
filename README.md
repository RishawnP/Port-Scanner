# PortScanner

This Python-based port scanner allows you to scan a range of ports on a remote server (IP address) to check which ports are open or closed. It includes features such as parallel port scanning, verbose output, custom timeouts, and scanning of common ports like HTTP, HTTPS, FTP, etc.

## Features

- **Port Scanning**: Scan a specific range of ports on a target IP address.
- **Verbose Output**: Option to enable detailed logging of the scan results.
- **Timeout Configuration**: Customize the timeout period for each port check.
- **Common Port Scanning**: Automatically scans a predefined list of common ports (e.g., HTTP, FTP).
- **Parallel Scanning**: Scans ports concurrently using threading, making the process faster.

## Requirements

- Python 3.x
- No external libraries are required. The script uses built-in Python libraries (`socket`, `threading`, `time`, and `sys`).

## How to Use

1. **Clone the repository** (if hosted on GitHub) or **download the script** (`port_scanner.py`).
   
2. **Run the script** using the following command:

    ```bash
    python port_scanner.py
    ```

3. The program will prompt you for the following inputs:
    - **IP address**: The target IP address to scan.
    - **Port range**: The starting and ending port numbers.
    - **Timeout period**: How long the script should wait for a connection on each port (in seconds).
    - **Verbose mode**: Whether you want detailed logs of the port scan (yes/no).
    
4. The results of the scan will be printed directly to the terminal, showing the status (open/closed) for each port.

### Example

```bash
Welcome to the enhanced Port Scanner!
Enter the IP address to scan: 192.168.1.1
Enter the start port number: 20
Enter the end port number: 25
Enter the timeout period in seconds (e.g., 1): 1
Do you want verbose output? (y/n): y

Scanning ports 20 to 25 on 192.168.1.1...

[+] Port 20 is CLOSED
[+] Port 21 is OPEN
[+] Port 22 is OPEN
[+] Port 23 is CLOSED
[+] Port 24 is CLOSED
[+] Port 25 is OPEN

Scanning common ports...
Scanning FTP on port 20...
[-] Port 20 is CLOSED
Scanning FTP Control on port 21...
[+] Port 21 is OPEN
...

Scan completed in 0.45 seconds.
