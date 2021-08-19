from selenium import webdriver
import os

#Pausar terminal
os.system("pause")

#limpar a tela
os.system('cls' if os.name == 'nt' else 'clear')

#Abrir navegador.
nav = webdriver.Chrome()

#Inserir URL no Browser.
url = "http://201.71.163.193/" 
nav.get(url)

#função que tenta logar ZTE
def tentar_logar():
	user = nav.find_element_by_xpath('//*[@id="Frm_Username"]')
	user.send_keys("multipro")

	senha = nav.find_element_by_xpath('//*[@id="Frm_Password"]')
	senha.send_keys("126462")

	entrar = nav.find_element_by_xpath('//*[@id="LoginId"]').click()

	try:
		teste = nav.find_element_by_xpath('//*[@id="Frm_Password"]')
		os.system('cls' if os.name == 'nt' else 'clear')
		print("######### ERROR #########")

	except:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("######### Logado #########")

tentar_logar()

     
    
