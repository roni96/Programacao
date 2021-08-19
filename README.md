

**Transformar em executável:**
~~~
>py -m pip install PyInstaller
>py -m PyInstaller arquivo.py --onefile
~~~

**Instalar bibliotecas**
~~~
py -m pip install pyautogui
~~~
**Instalar PIP**
~~~
sudo apt-get install python3-pip
~~~
**Atualizar PIP**
~~~
py -m pip install --upgrade pip
~~~
**instalar Webdriver win10**
~~~
C:\Users\i9\AppData\Local\Programs\Python\Python38-32
~~~
---

**Input de dados**
~~~python
ipadd = input("qual IP")
~~~

**Output de dados**
~~~python
print "hello word"
~~~

**The Zen of Python** <br>
~~~python
import this
~~~
**Estrutura condicional**
~~~python
if soma > 0:
     print "Maior que Zero."
elif soma = 0:
     print "Igual a Zero."
else:
     print "Menor que Zero."
~~~




**Estrutura de repetição**
~~~python
for x in range(2, 6):
  print(x)
~~~

~~~python
count = 0
while (count < 3):     
    count = count + 1
    print("Hello Geek") 
~~~

**Tratamento de exceções**
~~~python
try:
    código a tentar
except AlgumaExcecao:
    código a executar no caso da exceção
else:
    código a executar caso não ocorra exceção em try
finally:
    código que é executado sempre, independente de haver uma exceção em andamento ou não
~~~

**Interação com sistema operacional**
~~~python
import os
hostname = "google.com" #example
response = os.system("ping 1 ", hostname)

print('response')
~~~
**Funções**
~~~python
def my_function():
  print("Hello from a function")

my_function()
~~~

