import socket
import subprocess


class SnSNmap():
	
	def __init__(self):
		print("Scanners")
		
	def MainScan(self, ipscanning, pathsave):
		print("starting: " + ipscanning + " saving to " + pathsave)
		#-A -Pn
		#nmap --open -d -O -sV --max-scan-delay 10 --max-retries 2 --min-hostgroup 25 --min-parallelism 25 --top-ports 1000 -T4 -Pn --min-rate 1000 --script=vuln -oX 
		#p = subprocess.Popen("nmap -d --open -sS -vvv -O -sV --max-scan-delay 10 --max-retries 2 --min-hostgroup 25 --min-parallelism 25 -p- -T4 --min-rate 3000 -oX "+pathsave+"/master.xml " + ipscanning, stdout=subprocess.PIPE, shell=True)
		p = subprocess.Popen("nmap --open -T4 -sV --max-parallelism 100 -O -vvv -sS -p- --min-rate 10000 -oX "+pathsave+"/master.xml " + ipscanning, stdout=subprocess.PIPE, shell=True)
		(output, err) = p.communicate()
		p_status = p.wait()
		print("scan complete " + ipscanning)
		
	def PingNetwork(self, ipscan, pathsave):
		pingoutput = []
		p = subprocess.Popen("proxychains nmap -n -sn "+ipscan+"/24 -oX "+pathsave+"/ping.xml -oG - | awk '/Up$/{print $2}'", stdout=subprocess.PIPE, shell=True)
		(output, err) = p.communicate()
		p_status = p.wait()
		if "\n" in output:
			presults = output.split("\n")
			for l in presults:
				#print(l)
				pingoutput.append(str(l))
		return pingoutput
