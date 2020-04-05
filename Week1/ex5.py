#!/usr/bin/env python

# Device Information
mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

# First Device
mac1_split = mac1.split()
mac1_ipaddr = mac1_split[1]
mac1_macaddr = mac1_split[3]

# Second Device
mac2_split = mac2.split()
mac2_ipaddr = mac2_split[1]
mac2_macaddr = mac2_split[3]

# Third Device
mac3_split = mac3.split()
mac3_ipaddr = mac3_split[1]
mac3_macaddr = mac3_split[3]

column1 = "-" * 20
column2 = "-" * 20

print("{0:>20} {1:>20}".format("IP ADDR", "MAC ADDRESS"))
print("{0:20} {1:20}".format(column1, column2))
print("{0:>20} {1:>20}".format(mac1_ipaddr, mac1_macaddr))
print("{0:>20} {1:>20}".format(mac2_ipaddr, mac2_macaddr))
print("{0:>20} {1:>20}".format(mac2_ipaddr, mac2_macaddr))
