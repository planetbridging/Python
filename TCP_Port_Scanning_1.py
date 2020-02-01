import socket
from concurrent.futures.thread import ThreadPoolExecutor

server = "192.168.0.1"

def PScan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((server,port))
        return True
    except:
        return False

def FindPort(ip,port):
    if PScan(port):
        print(port)

with ThreadPoolExecutor(max_workers=65535) as executor:
    for x in range(1,65535):
        executor.submit(FindPort, server, x)
