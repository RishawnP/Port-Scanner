import socket
import threading
import time
import sys

# Function to check if a port is open
def check_port(ip, port, timeout, verbose):
    """Try to connect to the specified IP and port to see if it is open."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)  # Custom timeout for the connection
    try:
        result = sock.connect_ex((ip, port))  # connect_ex returns 0 if the port is open
        if result == 0:
            result_message = f"Port {port} is OPEN"
            if verbose:
                print(f"[+] {result_message}")
        else:
            result_message = f"Port {port} is CLOSED"
            if verbose:
                print(f"[-] {result_message}")
    except socket.error as e:
        if verbose:
            print(f"[!] Error on port {port}: {e}")
    finally:
        sock.close()

# Function to handle the scanning process with parallel threads
def scan_ports(ip, start_port, end_port, timeout, verbose):
    """Scan ports in the given range on the target IP."""
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=check_port, args=(ip, port, timeout, verbose))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# Function to scan common ports
def scan_common_ports(ip, timeout, verbose):
    """Scan a list of common ports (HTTP, HTTPS, etc.)."""
    common_ports = {
        20: 'FTP', 21: 'FTP Control', 22: 'SSH', 23: 'Telnet', 25: 'SMTP',
        53: 'DNS', 80: 'HTTP', 443: 'HTTPS', 8080: 'HTTP Proxy'
    }
    print("\nScanning common ports...")
    for port, service in common_ports.items():
        print(f"Scanning {service} on port {port}...")
        check_port(ip, port, timeout, verbose)

def main():
    """Main function to interact with the user."""
    print("Welcome to the enhanced Port Scanner!")
    
    ip = input("Enter the IP address to scan: ")
    try:
        start_port = int(input("Enter the start port number: "))
        end_port = int(input("Enter the end port number: "))
        timeout = float(input("Enter the timeout period in seconds (e.g., 1): "))
        verbose = input("Do you want verbose output? (y/n): ").lower() == 'y'

        print(f"\nScanning ports {start_port} to {end_port} on {ip}...\n")

        start_time = time.time()
        
        # Scan the specified range of ports
        scan_ports(ip, start_port, end_port, timeout, verbose)
        
        # Optionally scan common ports
        scan_common_ports(ip, timeout, verbose)
        
        end_time = time.time()
        print(f"\nScan completed in {end_time - start_time:.2f} seconds.")
        
    except ValueError:
        print("Invalid input. Please enter valid numbers for ports and timeout.")
    
if __name__ == "__main__":
    main()
