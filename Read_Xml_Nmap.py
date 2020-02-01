from xml.dom import minidom
from texttable import Texttable
xmldoc = minidom.parse('network.xml')
hosts = xmldoc.getElementsByTagName('host')
t = Texttable()
for h in hosts:
    address = h.getElementsByTagName('address')
    hostnames = h.getElementsByTagName('hostnames')
    ports = h.getElementsByTagName('port')
    vendor = ""
    ip = ""
    hostname = ""
    mac = ""

    for hn in hostnames:
        if len(hn.getElementsByTagName('hostname')) > 0:
            for names in hn.getElementsByTagName('hostname'):
                hostname = names.getAttribute("name")

    for a in address:
        vendor = a.getAttribute("vendor")
        if a.getAttribute("addrtype") == "mac":
            mac = a.getAttribute("addr")
        if a.getAttribute("addrtype") == "ipv4":
            ip = a.getAttribute("addr")
    t.add_rows([['ip', 'hostname', 'mac', 'vendor'], [ip,hostname,mac,vendor]])
    
    tport = Texttable()
    for p in ports:
        protocol = p.getAttribute("protocol")
        tcpport = ""
        if protocol == "tcp":
            tcpport = p.getAttribute("portid")
        for services in p.getElementsByTagName('service'):
            pname = services.getAttribute("name")
            pproduct = services.getAttribute("product")
            pversion = services.getAttribute("version")
            foundcpe = "no"
            for cpe in services.getElementsByTagName('cpe'):
                tcpe = cpe.firstChild.data
                tport.add_rows([['port', 'name', 'product', 'version', 'cpe'], [tcpport,pname,pproduct,pversion,tcpe]])
                foundcpe = "yes"
            if foundcpe == "no":
                tport.add_rows([['port', 'name', 'product', 'version', 'cpe'], [tcpport,pname,pproduct,pversion,""]])
    print("%s | %s | %s | %s"%(ip,hostname,mac,vendor))
    print (tport.draw())

#print (t.draw())
