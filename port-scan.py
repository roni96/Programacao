#
# Dev: Romilson Ramos     
# Estrutura do comando: port_scan.py rede porta
# https://www.linkedin.com/in/romilsonramos96/
#


import ipaddress, socket, sys, os
from tqdm import*

os.system('cls')
param = sys.argv[1:]

if(param[0] == 'help' or param[0] =='h'):
    print('+','='*55)
    print('| Port scan, desenvolvido por Romilson Ramos')
    print('+','='*55)
else:
    try:
        rede = ipaddress.ip_network(param[0],strict=False)
        port = int(param[1])
    except:
        print('ERRROOOR_Sintaxe_do_comando: esperado rede e porta')
        sys.exit()

    print( '+','='*55)
    print(f'| Realizar scan na rede {rede} na porta {port} TCP')
    print( '+','='*55)

    for ipadd in tqdm(rede):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(0.1)
        cod = s.connect_ex((str(ipadd),port))
        s.shutdown

        if cod == 0:
            tqdm.write(f'| IP:{ipadd} porta:{port} open')

    print( '+','='*55)
    print( '| Scan finalizado com sucesso!!!')
    print( '+','='*55)
