import socket
import sys
from datetime import datetime

#Ask the user for input (IP or Domain name)
user_input = input("Enter the target host to scan (e.g., 127.0.0.1 or scanme.nmap.org): ")

try:
    #Translate the hostname to an IPv4 address
    target_host = socket.gethostbyname(user_input)
except socket.gaierror:
    print("\nError: Hostname could not be resolved. Check your spelling or internet connection.")
    sys.exit()


print("-" * 50)
print(f"Scanning target IP: {target_host}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    # Let's check common ports: 21 (FTP), 22 (SSH), 80 (HTTP), 443 (HTTPS)
    ports_to_scan = [21, 22, 80, 443, 8080]
    
    for port in ports_to_scan:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        
        print(f"Checking Port {port}...")
        result = s.connect_ex((target_host, port))
        
        if result == 0:
            print(f"-> Port {port}: OPEN")
        else:
            print(f"-> Port {port}: CLOSED")
            
        s.close()

except KeyboardInterrupt:
    print("\nExiting script.")
    sys.exit()

except socket.error:
    print("\nCould not connect to the server.")
    sys.exit()