#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from scapy.all import *
from socket import *
from concurrent.futures.thread import ThreadPoolExecutor


# port_scan.py <host> <start_port>-<end_port>
host = "192.168.0.1"
portstrs = "1-65535".split('-')
start_port = int(portstrs[0])
end_port = int(portstrs[1])
target_ip = gethostbyname(host)
opened_ports = []
sport = RandShort()
target = "192.168.0.1"
def syn_scan(port):
	pkt = sr1(IP(dst=target)/TCP(sport=sport, dport=port, flags="S"), timeout=0.5, verbose=0)
	if pkt != None:
		if pkt.haslayer(TCP):
			if pkt[TCP].flags == 18:
				print(port)

def scan_port(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        opened_ports.append(port)
    else:
        syn_scan(target_ip,port)

def newsyn(port):
    packet = IP(dst=target)/TCP(dport=port,flags="S")
    response = sr1(packet,timeout=0.5,verbose=0)
    if response.haslayer(TCP) and response.getlayer(TCP).flags==0x12:
        print(port)
    sr(IP(dst=target)/TCP(dport=response.sport,flags="R"),timeout=0.5,verbose=0)

with ThreadPoolExecutor(max_workers=65000) as executor:
    for port in range(start_port, end_port):
        executor.submit(newsyn, port)

print("Opened ports:")
for i in opened_ports:
    print(i)
