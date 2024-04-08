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
def process_pcap_to_csv_testing(input_file, output_file):
    print(f"Processing {input_file} and saving selected fields to {output_file}...")
    packets = scapy.rdpcap(input_file)
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'Source IP', 'Destination IP', 'Source Port', 'Destination Port'])
        for packet in packets:
            if scapy.IP in packet and scapy.TCP in packet:
                timestamp = packet.time
                src_ip = packet[scapy.IP].src
                dst_ip = packet[scapy.IP].dst
                src_port = packet[scapy.TCP].sport
                dst_port = packet[scapy.TCP].dport
                writer.writerow([timestamp, src_ip, dst_ip, src_port, dst_port])
    print("CSV file saved.")


def process_pcap_to_csv_test2(input_file, output_file):
    print(f"Processing {input_file} and saving selected fields to {output_file}...")
    packets = scapy.rdpcap(input_file)
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'Source IP', 'Destination IP', 'Source Port', 'Destination Port',
                         'Sequence Number', 'Acknowledgment Number', 'Data Offset', 'Reserved', 'Flags',
                         'Window Size', 'Checksum', 'Urgent Pointer', 'Options'])
        for packet in packets:
            if scapy.IP in packet and scapy.TCP in packet:
                timestamp = packet.time
                src_ip = packet[scapy.IP].src
                dst_ip = packet[scapy.IP].dst
                src_port = packet[scapy.TCP].sport
                dst_port = packet[scapy.TCP].dport
                seq_num = packet[scapy.TCP].seq
                ack_num = packet[scapy.TCP].ack
                data_offset = packet[scapy.TCP].dataofs
                reserved = packet[scapy.TCP].reserved
                flags = packet[scapy.TCP].flags
                window_size = packet[scapy.TCP].window
                checksum = packet[scapy.TCP].chksum
                urgent_pointer = packet[scapy.TCP].urgptr
                options = packet[scapy.TCP].options
                writer.writerow([timestamp, src_ip, dst_ip, src_port, dst_port, seq_num, ack_num,
                                 data_offset, reserved, flags, window_size, checksum, urgent_pointer, options])
    print("CSV file saved.")

def process_pcap_to_csv(input_file, output_file):
    print(f"Processing {input_file} and saving selected fields to {output_file}...")
    packets = scapy.rdpcap(input_file)
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'Ethernet Source', 'Ethernet Destination', 'Ethernet Type',
                         'IP Version', 'IP Header Length', 'IP TOS', 'IP Total Length', 'IP Identification',
                         'IP Flags', 'IP Fragment Offset', 'IP TTL', 'IP Protocol', 'IP Checksum',
                         'IP Source', 'IP Destination', 'IP Options',
                         'TCP Source Port', 'TCP Destination Port', 'TCP Sequence Number', 'TCP Acknowledgment Number',
                         'TCP Data Offset', 'TCP Reserved', 'TCP Flags', 'TCP Window Size', 'TCP Checksum',
                         'TCP Urgent Pointer', 'TCP Options',
                         'UDP Source Port', 'UDP Destination Port', 'UDP Length', 'UDP Checksum',
                         'Raw Payload',
                         'DNS Transaction ID', 'DNS Query/Response', 'DNS OpCode', 'DNS Authoritative Answer',
                         'DNS Truncation', 'DNS Recursion Desired', 'DNS Recursion Available', 'DNS Reserved',
                         'DNS Response Code', 'DNS Question Count', 'DNS Answer Count', 'DNS NS Count',
                         'DNS Additional Count'])

        for packet in packets:
            timestamp = packet.time
            eth_src = packet[scapy.Ether].src if scapy.Ether in packet else ''
            eth_dst = packet[scapy.Ether].dst if scapy.Ether in packet else ''
            eth_type = packet[scapy.Ether].type if scapy.Ether in packet else ''

            ip_version = packet[scapy.IP].version if scapy.IP in packet else ''
            ip_ihl = packet[scapy.IP].ihl if scapy.IP in packet else ''
            ip_tos = packet[scapy.IP].tos if scapy.IP in packet else ''
            ip_len = packet[scapy.IP].len if scapy.IP in packet else ''
            ip_id = packet[scapy.IP].id if scapy.IP in packet else ''
            ip_flags = packet[scapy.IP].flags if scapy.IP in packet else ''
            ip_frag = packet[scapy.IP].frag if scapy.IP in packet else ''
            ip_ttl = packet[scapy.IP].ttl if scapy.IP in packet else ''
            ip_proto = packet[scapy.IP].proto if scapy.IP in packet else ''
            ip_chksum = packet[scapy.IP].chksum if scapy.IP in packet else ''
            ip_src = packet[scapy.IP].src if scapy.IP in packet else ''
            ip_dst = packet[scapy.IP].dst if scapy.IP in packet else ''
            ip_options = packet[scapy.IP].options if scapy.IP in packet else ''

            tcp_sport = packet[scapy.TCP].sport if scapy.TCP in packet else ''
            tcp_dport = packet[scapy.TCP].dport if scapy.TCP in packet else ''
            tcp_seq = packet[scapy.TCP].seq if scapy.TCP in packet else ''
            tcp_ack = packet[scapy.TCP].ack if scapy.TCP in packet else ''
            tcp_dataofs = packet[scapy.TCP].dataofs if scapy.TCP in packet else ''
            tcp_reserved = packet[scapy.TCP].reserved if scapy.TCP in packet else ''
            tcp_flags = packet[scapy.TCP].flags if scapy.TCP in packet else ''
            tcp_window = packet[scapy.TCP].window if scapy.TCP in packet else ''
            tcp_chksum = packet[scapy.TCP].chksum if scapy.TCP in packet else ''
            tcp_urgptr = packet[scapy.TCP].urgptr if scapy.TCP in packet else ''
            tcp_options = packet[scapy.TCP].options if scapy.TCP in packet else ''

            udp_sport = packet[scapy.UDP].sport if scapy.UDP in packet else ''
            udp_dport = packet[scapy.UDP].dport if scapy.UDP in packet else ''
            udp_len = packet[scapy.UDP].len if scapy.UDP in packet else ''
            udp_chksum = packet[scapy.UDP].chksum if scapy.UDP in packet else ''

            raw_load = packet[scapy.Raw].load if scapy.Raw in packet else ''

            dns_id = packet[scapy.DNS].id if scapy.DNS in packet else ''
            dns_qr = packet[scapy.DNS].qr if scapy.DNS in packet else ''
            dns_opcode = packet[scapy.DNS].opcode if scapy.DNS in packet else ''
            dns_aa = packet[scapy.DNS].aa if scapy.DNS in packet else ''
            dns_tc = packet[scapy.DNS].tc if scapy.DNS in packet else ''
            dns_rd = packet[scapy.DNS].rd if scapy.DNS in packet else ''
            dns_ra = packet[scapy.DNS].ra if scapy.DNS in packet else ''
            dns_z = packet[scapy.DNS].z if scapy.DNS in packet else ''
            dns_rcode = packet[scapy.DNS].rcode if scapy.DNS in packet else ''
            dns_qdcount = packet[scapy.DNS].qdcount if scapy.DNS in packet else ''
            dns_ancount = packet[scapy.DNS].ancount if scapy.DNS in packet else ''
            dns_nscount = packet[scapy.DNS].nscount if scapy.DNS in packet else ''
            dns_arcount = packet[scapy.DNS].arcount if scapy.DNS in packet else ''

            print("Timestamp:", timestamp)
            print("Ethernet Source:", eth_src)
            print("Ethernet Destination:", eth_dst)
            print("Ethernet Type:", eth_type)
            print("IP Version:", ip_version)
            print("IP Header Length:", ip_ihl)
            print("IP TOS:", ip_tos)
            print("IP Total Length:", ip_len)
            print("IP Identification:", ip_id)
            print("IP Flags:", ip_flags)
            print("IP Fragment Offset:", ip_frag)
            print("IP TTL:", ip_ttl)
            print("IP Protocol:", ip_proto)
            print("IP Checksum:", ip_chksum)
            print("IP Source:", ip_src)
            print("IP Destination:", ip_dst)
            print("IP Options:", ip_options)
            print("TCP Source Port:", tcp_sport)
            print("TCP Destination Port:", tcp_dport)
            print("TCP Sequence Number:", tcp_seq)
            print("TCP Acknowledgment Number:", tcp_ack)
            print("TCP Data Offset:", tcp_dataofs)
            print("TCP Reserved:", tcp_reserved)
            print("TCP Flags:", tcp_flags)
            print("TCP Window Size:", tcp_window)
            print("TCP Checksum:", tcp_chksum)
            print("TCP Urgent Pointer:", tcp_urgptr)
            print("TCP Options:", tcp_options)
            print("UDP Source Port:", udp_sport)
            print("UDP Destination Port:", udp_dport)
            print("UDP Length:", udp_len)
            print("UDP Checksum:", udp_chksum)
            print("Raw Payload:", raw_load)
            print("DNS Transaction ID:", dns_id)
            print("DNS Query/Response:", dns_qr)
            print("DNS OpCode:", dns_opcode)
            print("DNS Authoritative Answer:", dns_aa)
            print("DNS Truncation:", dns_tc)
            print("DNS Recursion Desired:", dns_rd)
            print("DNS Recursion Available:", dns_ra)
            print("DNS Reserved:", dns_z)
            print("DNS Response Code:", dns_rcode)
            print("DNS Question Count:", dns_qdcount)
            print("DNS Answer Count:", dns_ancount)
            print("DNS NS Count:", dns_nscount)
            print("DNS Additional Count:", dns_arcount)
            print("---")

            writer.writerow([timestamp, eth_src, eth_dst, eth_type,
                             ip_version, ip_ihl, ip_tos, ip_len, ip_id,
                             ip_flags, ip_frag, ip_ttl, ip_proto, ip_chksum,
                             ip_src, ip_dst, ip_options,
                             tcp_sport, tcp_dport, tcp_seq, tcp_ack,
                             tcp_dataofs, tcp_reserved, tcp_flags, tcp_window, tcp_chksum,
                             tcp_urgptr, tcp_options,
                             udp_sport, udp_dport, udp_len, udp_chksum,
                             raw_load,
                             dns_id, dns_qr, dns_opcode, dns_aa,
                             dns_tc, dns_rd, dns_ra, dns_z,
                             dns_rcode, dns_qdcount, dns_ancount, dns_nscount,
                             dns_arcount])
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