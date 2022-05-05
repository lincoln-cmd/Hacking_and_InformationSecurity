# https://scribblinganything.tistory.com/235?category=987545

import nmap
nm = nmap.PortScanner()
print(nm.scan('12.70.0.1', '22-443'))
