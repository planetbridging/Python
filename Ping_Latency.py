import ipaddress
import time
import random
import struct
import select
import socket
from concurrent.futures.thread import ThreadPoolExecutor


def chk(data):
    x = sum(x << 8 if i % 2 else x for i, x in enumerate(data)) & 0xFFFFFFFF
    x = (x >> 16) + (x & 0xFFFF)
    x = (x >> 16) + (x & 0xFFFF)
    return struct.pack('<H', ~x & 0xFFFF)


def ping(addr, timeout=1, number=1, data=b''):
    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as conn:
        payload = struct.pack('!HH', random.randrange(0, 65536), number) + data

        conn.connect((addr, 80))
        conn.sendall(b'\x08\0' + chk(b'\x08\0\0\0' + payload) + payload)
        start = time.time()

        while select.select([conn], [], [], max(0, start + timeout - time.time()))[0]:
            data = conn.recv(65536)
            if len(data) < 20 or len(data) < struct.unpack_from('!xxH', data)[0]:
                continue
            if data[20:] == b'\0\0' + chk(b'\0\0\0\0' + payload) + payload:
                return time.time() - start



def PingIP(ip):
    results = ping(ip)
    if results is not None:
        print(ip)
        print(results)


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=255) as executor:
        for i in range(1, 255):
            sendto = "192.168.0."+str(i)
            executor.submit(PingIP,sendto )
        executor.submit(PingIP,"107.180.51.82" )  # ip of http://declair.in/
        executor.submit(PingIP,"127.0.0.1" )
    print("Complete")

