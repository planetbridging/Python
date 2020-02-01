# port scanner
import argparse
from concurrent.futures.thread import ThreadPoolExecutor
from scapy.all import *



# output format # TODO make prettier
def print_ports(port, state):
	#print("%s | %s" % (port, state))
	r = port

# syn scan
def syn_scan(target, ports):
	print("syn scan on, %s with ports %s" % (target, ports))
	sport = RandShort()
	for port in ports:
		pkt = sr1(IP(dst=target)/TCP(sport=sport, dport=port, flags="S"), timeout=1, verbose=0)
		if pkt != None:
			if pkt.haslayer(TCP):
				if pkt[TCP].flags == 20:
					print_ports(port, "Closed")
				elif pkt[TCP].flags == 18:
					print_ports(port, "Open")
				else:
					print_ports(port, "TCP packet resp / filtered")
			elif pkt.haslayer(ICMP):
				print_ports(port, "ICMP resp / filtered")
			else:
				print_ports(port, "Unknown resp")
				print(pkt.summary())
		else:
			print_ports(port, "Unanswered")

target = "192.168.0.1"
sport = RandShort()
def syn_scans(port):
	#print("syn scan on, %s with ports %s" % (target, ports))
	pkt = sr1(IP(dst=target)/TCP(sport=sport, dport=port, flags="S"), timeout=1, verbose=0)
	if pkt != None:
		if pkt.haslayer(TCP):
			if pkt[TCP].flags == 20:
				print_ports(port, "Closed")
			elif pkt[TCP].flags == 18:
				print(port)
			else:
				print_ports(port, "TCP packet resp / filtered")
		elif pkt.haslayer(ICMP):
			print_ports(port, "ICMP resp / filtered")
		else:
			print_ports(port, "Unknown resp")
			print(pkt.summary())
	else:
		print_ports(port, "Unanswered")

with ThreadPoolExecutor(max_workers=65000) as executor:
    for port in range(1, 65535):
        executor.submit(syn_scans, port)

print("efe")

#arr =[]
#for port in range(1, 65535):
#	arr.append(port)

#syn_scan("192.168.0.1",arr)

