#!/usr/bin/env python

from __future__ import print_function, unicode_literals

google_ip = '2607:f8b0:4000:806::200e'
FACEBOOK_IP = '2a03:2880:f134:183:face:b00c:0:25de'
GmA1L_1P = '2607:f8b0:4000:815::2005'

compare_1 = google_ip == FACEBOOK_IP
compare_2 = google_ip != GmA1L_1P

print(compare_1)
print(compare_2)
