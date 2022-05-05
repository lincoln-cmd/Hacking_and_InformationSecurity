# https://scribblinganything.tistory.com/260

import nmap
import ipaddress
import re

#print("test")
port_regex = re.compile("([0-9]+){1, 5} - ([0-0]+){1, 5}")
ip_regex1 = re.compile("^\d")
nmap_scan = nmap.PortScanner()

while True:
    ip_addr_input = input("Insert IP address(ex: 192.168.1.0) : ")
    try:
        ip_regex1_valid = ip_regex1.search(ip_addr_input.replace(" " ,""))
        if ip_regex1_valid:
            ip_addr = ipaddress.ip_address(ip_addr_input)
            print(ip_addr)
            print(type(ip_addr))
            break
    except:
        printf("wrong address")

while True:
    port_min = 0
    port_max = 65535
    port_range = input("Decide port range(ex: 0-65535) :")
    port_range_valid = port_regex.search(port_range.replace(" " ,""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

for port in range(port_min, port_max + 1):
    try:
        port_condition = nmap_scan.scan(ip_addr_input, str(port))
        print(port_condition)
        state = (port_condition['scan'][ip_addr_input]['tcp'][port]['state'])
    except:
        print(f"{port} is closed")
