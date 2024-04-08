import subprocess
import requests
import time

def send_get_requests(url, total_size_mb=1, payload_size_bytes=1024):
    total_requests = (total_size_mb * 1024 * 1024) // payload_size_bytes
    payload = 'a' * payload_size_bytes  # Generate a small payload to include in each GET request

    for i in range(total_requests):
        full_url = f"{url}?data={payload}"
        response = requests.get(full_url)

def ping_host(ip):
    subprocess.run(['ping', '-c', '4', ip])

def run_nmap_scan(ip, port):
    subprocess.run(['sudo', 'nmap', ip, '-p', port, '-vv'])

# Usage
ping_host('192.168.0.222')
print("sending bulk http request")
send_get_requests('http://192.168.0.222:8120/cybersecurity', total_size_mb=1)
run_nmap_scan('192.168.0.222', '8120')
run_nmap_scan('192.168.0.222', '-')
