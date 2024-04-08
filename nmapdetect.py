import scapy.all as scapy
import csv
import time
import argparse

# Function to capture packets on the specified port and save to a PCAP file
def capture_packets(output_file, port, duration):
    print(f"Capturing packets on port {port} for {duration} seconds and saving to {output_file}...")
    packets = scapy.sniff(filter=f"port {port}", timeout=duration)
    scapy.wrpcap(output_file, packets)
    print("Packet capture completed.")

# Function to process PCAP file and save selected fields to a CSV file
def process_pcap_to_csvold(input_file, output_file):
    print(f"Processing {input_file} and saving selected fields to {output_file}...")
    packets = scapy.rdpcap(input_file)
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'Source IP', 'Destination IP', 'Source Port', 'Destination Port', 'Nmap Detection'])

        for packet in packets:
            timestamp = packet.time
            src_ip = packet[scapy.IP].src if scapy.IP in packet else ''
            dst_ip = packet[scapy.IP].dst if scapy.IP in packet else ''
            src_port = packet[scapy.TCP].sport if scapy.TCP in packet else ''
            dst_port = packet[scapy.TCP].dport if scapy.TCP in packet else ''

            # Detect Nmap scan
            nmap_detected = False
            if scapy.TCP in packet:
                flags = packet[scapy.TCP].flags
                if flags == 0x02:  # SYN scan
                    nmap_detected = True
                elif flags == 0x29:  # FIN, PSH, URG scan
                    nmap_detected = True
                elif flags == 0x00:  # Null scan
                    nmap_detected = True
                elif flags == 0x29:  # Xmas scan
                    nmap_detected = True
                elif flags == 0x10:  # ACK scan
                    nmap_detected = True
                elif flags == 0xc0:  # Window scan
                    nmap_detected = True

            writer.writerow([timestamp, src_ip, dst_ip, src_port, dst_port, nmap_detected])
    print("CSV file saved.")

def process_pcap_to_csv(input_file, output_file):
    print(f"Processing {input_file} and saving selected fields to {output_file}...")
    packets = scapy.rdpcap(input_file)
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'Source IP', 'Destination IP', 'Source Port', 'Destination Port',
                         'TCP Flags', 'Payload', 'Nmap Detection'])

        for packet in packets:
            timestamp = packet.time
            src_ip = packet[scapy.IP].src if scapy.IP in packet else ''
            dst_ip = packet[scapy.IP].dst if scapy.IP in packet else ''
            src_port = packet[scapy.TCP].sport if scapy.TCP in packet else ''
            dst_port = packet[scapy.TCP].dport if scapy.TCP in packet else ''
            tcp_flags = packet[scapy.TCP].flags if scapy.TCP in packet else ''
            payload = packet[scapy.Raw].load if scapy.Raw in packet else ''

            # Detect Nmap scan
            nmap_detected = False
            if scapy.TCP in packet:
                flags = packet[scapy.TCP].flags
                if flags == 0x02:  # SYN scan
                    nmap_detected = True
                elif flags == 0x29:  # FIN, PSH, URG scan
                    nmap_detected = True
                elif flags == 0x00:  # Null scan
                    nmap_detected = True
                elif flags == 0x29:  # Xmas scan
                    nmap_detected = True
                elif flags == 0x10:  # ACK scan
                    nmap_detected = True
                elif flags == 0xc0:  # Window scan
                    nmap_detected = True

            writer.writerow([timestamp, src_ip, dst_ip, src_port, dst_port, tcp_flags, payload, nmap_detected])
    print("CSV file saved.")

# Main program
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capture packets on a specific port and save to CSV")
    parser.add_argument("-p", "--port", type=int, default=80, help="Port number to capture packets on (default: 80)")
    parser.add_argument("-o", "--output", default="captured_packets.pcap", help="Output PCAP file name (default: captured_packets.pcap)")
    parser.add_argument("-c", "--csv", default="packet_data.csv", help="Output CSV file name (default: packet_data.csv)")
    parser.add_argument("-d", "--duration", type=int, default=5, help="Capture duration in seconds (default: 5)")
    args = parser.parse_args()

    pcap_file = args.output
    csv_file = args.csv
    port = args.port
    capture_duration = args.duration

    # Capture packets and save to PCAP file
    capture_packets(pcap_file, port, capture_duration)

    # Process PCAP file and save selected fields to CSV file
    process_pcap_to_csv(pcap_file, csv_file)