import socket
from datetime import datetime

print("=" * 50)
print("        PYTHON PORT SCANNER")
print("=" * 50)

target = input("Enter Target IP or Domain: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid Host")
    exit()

print(f"\nScanning Target: {target}")
print(f"IP Address: {target_ip}")
print("Started at:", datetime.now())
print("-" * 50)

try:
    for port in range(1, 1025):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(0.5)

        result = scanner.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port {port} is OPEN")

        scanner.close()

except KeyboardInterrupt:
    print("\nScan Stopped.")