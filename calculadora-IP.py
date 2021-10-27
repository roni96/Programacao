#
# Dev: Romilson Ramos
# https://www.linkedin.com/in/romilsonramos96/
#

import ipaddress,os
from tqdm import tqdm

os.system('cls')
print( '+','='*55)
param = input('| Digite o IP com prefixo: ')
print( '+','='*55)
network = ipaddress.IPv4Network(param, strict=False) 

hosts = []
for i in tqdm(network):
    hosts.append(i)

tamanho = len(hosts)
host_val = tamanho - 2

os.system('cls')
print( '+','='*55)
print(f'| Rede: {network}')
print(f'| Primeiro host: {hosts[1]}')
print(f'| Ultimo host: {hosts[tamanho-2]}')
print(f'| Broadcast: {hosts[tamanho-1]}')
print( '+','='*55)
