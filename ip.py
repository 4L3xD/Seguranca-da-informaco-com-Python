#Default Python3
import ipaddress

# IP
#ip = '192.168.0.1'
#endereco = ipaddress.ip_address(ip)
#print(endereco)

# REDE
ip = "192.168.0.1/24"
rede = ipaddress.ip_network(ip, strict=False)

for ip in rede:
    print(ip)