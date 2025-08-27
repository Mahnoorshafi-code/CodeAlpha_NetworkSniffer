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
