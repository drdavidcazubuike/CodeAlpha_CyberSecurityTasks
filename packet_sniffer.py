from scapy.all import sniff, IP

def process_packet(packet):
    if packet.haslayer(IP):
        ip = packet[IP]
        print("\n--- Packet Captured ---")
        print("Source IP:", ip.src)
        print("Destination IP:", ip.dst)
        print("Protocol:", ip.proto)

print("🔍 Sniffer started... generate some internet activity!")
print("Press Ctrl + C to stop\n")

sniff(prn=process_packet, count=10)
