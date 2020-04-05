#!/usr/bin/env python

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
version_split = show_version.split()
model = version_split[1]
serial_number = version_split[2]

compare1 = "Cisco" in model
compare2 = "811" in serial_number

print(compare1)
print(compare2)
