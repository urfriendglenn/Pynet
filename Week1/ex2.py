#!/usr/bin/env python

ip_addr = input("Enter an IP address: ")

ip_split = ip_addr.split('.')

octets = []
for i in ip_split:
    x = int(i)
    octets.append(x)

octets_bin = []
for i in octets:
    x = bin(i)
    octets_bin.append(x)

octets_hex = []
for i in octets:
    x = hex(i)
    octets_hex.append(x)

print("{:^15}{:^15}{:^15}{:^15}".format("Octet 1", "Octet 2", "Octet 3", "Octet 4"))
print("-" * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(*octets))
print("{:^15}{:^15}{:^15}{:^15}".format(*octets_bin))
print("{:^15}{:^15}{:^15}{:^15}".format(*octets_hex))
print("-" * 60)
