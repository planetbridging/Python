import scapy.all as scapy
import csv

# Function to capture packets on port 80 and save to a PCAP file
def capture_packets(output_file):
    print(f"Capturing packets on port 80 and saving to {output_file}...")
    packets = scapy.sniff(filter="port 80", count=10)  # Capture 10 packets on port 80
    scapy.wrpcap(output_file, packets)
    print("Packet capture completed.")

# Function to read packets from a PCAP file and print packet information
def read_packets(input_file):
    print(f"Reading packets from {input_file}...")
    packets = scapy.rdpcap(input_file)
    for packet in packets:
        print("Packet:")
        print(packet.summary())
        print("Source IP:", packet[scapy.IP].src)
        print("Destination IP:", packet[scapy.IP].dst)
        print("Source Port:", packet[scapy.TCP].sport)
        print("Destination Port:", packet[scapy.TCP].dport)
        print("Payload:")
        print(packet[scapy.Raw].load if scapy.Raw in packet else "No payload")
        print("---")

# Function to save selected packet fields to a CSV file
def save_to_csv(input_file, output_file):
    print(f"Saving selected fields from {input_file} to {output_file}...")
    packets = scapy.rdpcap(input_file)
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Source IP', 'Destination IP', 'Source Port', 'Destination Port'])
        for packet in packets:
            writer.writerow([
                packet[scapy.IP].src,
                packet[scapy.IP].dst,
                packet[scapy.TCP].sport,
                packet[scapy.TCP].dport
            ])
    print("CSV file saved.")

# Main program
pcap_file = "captured_packets.pcap"
csv_file = "packet_data.csv"

# Capture packets and save to PCAP file
capture_packets(pcap_file)

# Read packets from PCAP file and print packet information
read_packets(pcap_file)

# Save selected packet fields to CSV file
save_to_csv(pcap_file, csv_file)