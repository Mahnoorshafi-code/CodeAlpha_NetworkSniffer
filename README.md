# Network Sniffer

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Example Output](#example-output)  
6. [Screenshots](#screenshots)  
7. [Technical Details](#technical-details)  
8. [Contributing](#contributing)  
9. [License](#license)  

---

## Project Overview
The *Network Sniffer* is a Python-based tool that captures and analyzes network packets in real-time using *Scapy* and *Npcap*. It helps monitor network traffic, understand protocols, and detect suspicious activity. This project is ideal for learning network security, packet analysis, and protocol behavior.  

---

## Features
- Capture live network packets.  
- Display packet details: source IP, destination IP, protocol, payload.  
- Filter packets by protocol (TCP, UDP, ICMP, etc.).  
- Save captured packets to a file.  
- Command-line interface for simplicity.  

---

## Installation

### Prerequisites
- Python 3.x  
- [Npcap](https://nmap.org/npcap/) installed on Windows (required for packet capturing)  
- Python library: Scapy  

### Steps
1. Install Python: [Python Downloads](https://www.python.org/downloads/)  
2. Install Scapy:
```bash
pip install scapy

Clone this repository:

git clone Mahnoorshafi-code/CodeAlpha_NetworkSniffer cd network-sniffer 

Usage

Run the sniffer:
python sniffer.py 
Options:

Capture all packets:

python sniffer.py --all 

Filter packets by protocol:

python sniffer.py --protocol TCP 

Save captured packets:

python sniffer.py --save captured_packets.txt 
Captured packets display:

Source IP

Destination IP

Protocol

Packet size

Example Output

When running the sniffer, the output in the terminal may look like this:
Packet #1: Source IP: 192.168.1.10 Destination IP: 192.168.1.1 Protocol: TCP Length: 60 bytes Payload: 48656c6c6f20576f726c64 Packet #2: Source IP: 192.168.1.15 Destination IP: 8.8.8.8 Protocol: ICMP Length: 84 bytes Payload: 080045000054a6f400004001f6b8c0a8010fc0a80101 
You can filter specific protocols or save this output to a file for analysis.

Screenshots

1. Capturing packets
2. Filtering TCP packets
3. Packet details

Make sure screenshots are saved in a folder named screenshots in your repository.

Technical Details

Language: Python 3.x

Libraries: Scapy

Packet Capturing: Npcap (Windows)

Supported Protocols: TCP, UDP, ICMP, ARP

Platform: Windows / Linux

How it works:
The sniffer listens on the network interface using Npcap, captures packets with Scapy, and parses headers to extract IP addresses, ports, protocol type, and payload. Users can filter packets by protocol or save them for further analysis.

Contributing

Contributions are welcome!

Fork the repository

Create a branch for your feature

Submit a pull request

License

This project is licensed under the MIT License.
