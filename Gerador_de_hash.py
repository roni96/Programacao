#
# Dev: Romilson Ramos     
# Versão Beta ©
#

import hashlib, os

os.system('cls')
print('+','='*80)
entrada = input('| Entre a string para ser passada para hashe: ')
print('+','='*80)
print('| Digita a opcao de algoritimo')
print('| (1) - MD5')
print('| (2) - SHA1')
print('| (3) - SHA256')
print('| (4) - SHA512')
print('+','='*80)
opc = int(input('| Entre a opcao desejada: '))

if opc == 1:
    resultado = hashlib.md5(entrada.encode('utf-8'))
elif opc == 2:
    resultado = hashlib.sha1(entrada.encode('utf-8'))
elif opc == 3:
    resultado = hashlib.sha256(entrada.encode('utf-8'))
elif opc == 4:
    resultado = hashlib.sha512(entrada.encode('utf-8'))
else:
    print('| Opcao nao valida, saindo do programa!')

os.system('cls')
print('+','='*80)
print(f'| String: {entrada}')
print(f'| Hash: {resultado.hexdigest()}')
print('+','='*80)
