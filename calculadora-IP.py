#
# Dev: Romilson Ramos     
# Versão Beta ©
#

import ipaddress
from tqdm import tqdm

#Abrir arquivo
arq_resultado = open('arquivo.txt', 'r')
#Criar lista
resultado = arq_resultado.readlines()

#Solicita a rede ou IP ao usuário.
rede = input('Qual rede? ')
#Estanciado o objeto network que vai receber a rede do IP fornecido anteriormente
network = ipaddress.IPv4Network(rede) 

for x in tqdm(network.hosts()):
	resultado.append("{}\n".format(x))   # insira seu conteúdo

arq_resultado = open('arquivo.txt', 'w') # Abre novamente o arquivo (escrita)
arq_resultado.writelines(resultado)    # escreva o conteúdo criado anteriormente nele.
arq_resultado.close()
