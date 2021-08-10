
**Instalar bibliotecas**
~~~python
py -m pip install pyautogui
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

~~~
![image](https://user-images.githubusercontent.com/41062660/127602867-46fc5822-d5f9-4387-b889-9fa426779d1a.png) ![image](https://user-images.githubusercontent.com/41062660/127602991-02b845b5-33e7-45f0-a47d-d83675596038.png) ![image](https://user-images.githubusercontent.com/41062660/127603035-d52fe9d9-673e-40e0-b94a-8c112ee95a0f.png)




**Estrutura de repetição**
~~~python
for x in range(2, 6):
  print(x)
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

