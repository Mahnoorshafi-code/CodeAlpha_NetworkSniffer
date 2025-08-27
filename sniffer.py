from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:  # Only process IP packets
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto
        print(f"Source: {src} → Destination: {dst} | Protocol: {proto}")

# Capture 50 packets
sniff(filter="ip", prn=packet_callback, count=50)
