from ipaddress import *
ip_net = ip_network("192.168.32.96/255.255.255.224")
n = 0
for ip_add in ip_net:
    ip_add = bin(int(ip_add))[2:]
    if ip_add.count("1") % 2 == 0:
        n += 1
print(n)
# print(bin(155)[2:])
# print(int("011011", 2))
# print(bin(248)[2:], bin(105)[2:], bin(101)[2:])
# print(int("00101100101", 2))
# print(bin(53)[2:].rjust(8, "0"), bin(25)[2:].rjust(8, "0"))
