import nmap
nm = nmap.PortScanner()
machine = nm.scan('192.168.0.1', arguments='-O')
print(machine['scan']['192.168.0.1']['osmatch'][0]['osclass'][0]['osfamily'])
