
~~~python
import	socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    s.connect(("www.python.org", 800))
    print('port open')
except:
    print('port closed')
~~~

~~~python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.1)
codigo = s.connect_ex(('bancocn.com', 666))

print(codigo)
~~~

~~~python
import socket

print('+---------------------------+')
print('|    Port scan V1.0         |')
print('+---------------------------+')
ipadd = input('Endereço : ')

try:
    for port in range(0, 1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        codigo = s.connect_ex((ipadd, port))

        if codigo == 0:
            print('port ',port,' open')
except:
    print()

print('+---------------------------+')
print('|Port scan finished')
print('+---------------------------+')
~~~
