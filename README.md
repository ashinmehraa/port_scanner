# Simple Python Port Scanner

A lightweight, command-line TCP port scanner built entirely with Python's native `socket` library. 

This project was developed to demonstrate fundamental networking concepts, specifically how the OS interacts with the Transport Layer (TCP) to establish connections and handle DNS resolution.

## Features
* **DNS Resolution:** Automatically resolves human-readable domain names (e.g., `scanme.nmap.org`) into IPv4 addresses using `socket.gethostbyname`.
* **TCP Connect Scanning:** Utilizes standard 3-way handshakes to verify if a port is actively accepting connections.
* **Targeted Scanning:** Scans a predefined list of the most common service ports (FTP, SSH, HTTP, HTTPS) for rapid execution rather than iterating through all 65,535 ports sequentially.
* **Graceful Error Handling:** Catches keyboard interrupts (`Ctrl+C`) and DNS resolution failures without throwing raw stack traces to the user.

## Prerequisites
* Python 3.x
* No external libraries required (Uses built-in `socket`, `sys`, and `datetime`).

## Usage
1. Clone this repository to your local machine.
2. Run the script via the terminal:
   ```bash
   python port_scanner.py
