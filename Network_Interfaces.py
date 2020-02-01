import itertools
from netifaces import interfaces, ifaddresses, AF_INET
import psutil

#results = psutil.net_if_addrs()
#print(results)
#for i in results:
#    print(i)

def get_network():
    network = psutil.net_io_counters(pernic=True)
    ifaces = psutil.net_if_addrs()
    networks = list()
    for k, v in ifaces.items():
        ip = v[1].address
        data = network[k]
        ifnet = dict()
        ifnet['ip'] = ip
        ifnet['iface'] = k
        ifnet['sent'] = '%.2fMB' % (data.bytes_sent/1024/1024)
        ifnet['recv'] = '%.2fMB' % (data.bytes_recv/1024/1024)
        ifnet['packets_sent'] = data.packets_sent
        ifnet['packets_recv'] = data.packets_recv
        ifnet['errin'] = data.errin
        ifnet['errout'] = data.errout
        ifnet['dropin'] = data.dropin
        ifnet['dropout'] = data.dropout
        networks.append(ifnet)
    return networks

def get_network_noloopback():
    network = psutil.net_io_counters(pernic=True)
    ifaces = psutil.net_if_addrs()
    networks = list()
    iplst = []
    for k, v in ifaces.items():
        ip = v[1].address
        data = network[k]
        ifnet = dict()
        ifnet['ip'] = ip
        ifnet['iface'] = k
        if "loopback" not in k.lower():
            print(ifnet['iface'])
            iplst.append(ip)
        networks.append(ifnet)
    return iplst

print(get_network_noloopback())

links = filter(None, (ifaddresses(x).get(AF_INET) for x in interfaces()))
links = itertools.chain(*links)
ip_addresses = [x for x in links]

#print(netifaces.gateways())
