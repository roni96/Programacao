# coding: utf-8

import	socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    s.connect(("www.python.org", 800))
    print('port open')
except:
    print('port closed')

