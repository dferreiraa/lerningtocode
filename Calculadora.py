import math
from math import degrees
from time import sleep
def repitir():
    refazer= input('''Deseja fazer uma nova operação? 
    s - Sim
    n - Não
    ''')

    if refazer == 's':
        calculo()

    else:
        print("Até Mais")

def calculo():
    operacao = input('''Selecione a operção que voce quer fazer:
    1. Soma
    2. Subtração 
    3. Mutiplicação
    4. Divisão
    5. Seno
    ''')
    if operacao == '1':
        sleep(2)
        soma()
    elif operacao == '2':
        subtracao()
    elif operacao == '3':
        multiplicação()
    elif operacao == '4':
        divisão()
    elif operacao == '5':
        seno()



def soma():
    x= int(input("Insira o primeiro valor: "))
    y= int(input("Insira o segundo valor: "))
    sleep(1)
    print(x, "+", y, "=")
    print(x+y)

def subtracao():
    x= float(input("Insira o primeiro valor: "))
    y= float(input("Insira o segundo valor: "))
    sleep(1)
    print(x, "-", y, "=")
    print(x-y)

def multiplicação():
    x= int(input("Insira o primeiro valor: "))
    y= int(input("Insira o segundo valor: "))
    sleep(1)
    print(x ,"*",y, "=")
    print(x**y)

def divisão():
    x = int(input("Insira o primeiro valor: "))
    y = int(input("Insira o segundo valor: "))
    sleep(1)
    print(x, "/", y, "=")
    print(x // y)

def seno():
    x= int(input("Insira o valor do seno a ser calculado: "))
    print("O seno é: ", math.sin(x))
    sleep(2)




print("Bem vindo ao meu exercicio de funções")
sleep(3)
calculo()
repitir()

