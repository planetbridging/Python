import ast
import json


def GetJsonFind(data,find):
    json_data = ast.literal_eval(data)
    return json_data[find]

n = "{'hostnames': [{'name': 'dlinkrouter', 'type': 'PTR'}], 'addresses': {'ipv4': '192.168.0.1', 'mac': '00:11:22:33:44:55'}, 'vendor': {'00:11:22:33:44:55': 'D-Link International'}, 'status': {'state': 'up', 'reason': 'arp-response'}, 'tcp': {123: {'state': 'open', 'reason': 'syn-ack', 'name': 'upnp', 'product': 'MiniUPnP', 'version': '1.6', 'extrainfo': 'Netgear SDK 4.3.0.0; UPnP 1.0', 'conf': '10', 'cpe': 'cpe:/a:'}}}"
json_data = ast.literal_eval(n)

for key, value in json_data.items():
    print(key)
    print(value)
    hostname = ""
    ipv4 = ""
    mac = ""
    tcpport = ""
    tcpproduct = ""
    tcpname = ""
    tcpversion = ""
    tcpextrainfo = ""
    tcpcpe = ""
    if "hostnames" in key:
        if isinstance(value, list):
            hostname = ast.literal_eval(str(value[0]))["name"]
    if "addresses" in key:
        ipv4 = ast.literal_eval(str(value))["ipv4"]
        mac = ast.literal_eval(str(value))["mac"]
    if "tcp" in key:
        tcpitems = ast.literal_eval(str(value))
        for k, v in tcpitems.items():
            tcpport = k
            tcpitemsval = ast.literal_eval(str(v))
            tcpproduct = tcpitemsval["product"]
            tcpversion = tcpitemsval["version"]
            tcpextrainfo = tcpitemsval["extrainfo"]
            tcpcpe = tcpitemsval["cpe"]
