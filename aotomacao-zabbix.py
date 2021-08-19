from selenium import webdriver
import os

#limpar a tela
os.system('cls' if os.name == 'nt' else 'clear')

url = "http://172.16.254.216/" 
print("Conectando a "+url)


nav = webdriver.Chrome()
nav.get(url)

user = nav.find_element_by_xpath('//*[@id="name"]')
user.send_keys("romilson.ramos")

senha = nav.find_element_by_xpath('//*[@id="password"]')
senha.send_keys("redes8486")

entrar = nav.find_element_by_xpath('//*[@id="enter"]').click()


