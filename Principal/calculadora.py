# Conversão de binário para inteiro int("numeroEmBinario", 2)
from time import sleep


def funcaoEscritaInicial():
    print('---CALCULADORA DE BINÁRIOS---')
    sleep(0.5)
    print('|||||||||||||||       |||||||||||||||       |||||||||||||||')
    print('|||         |||       |||         |||       |||            ')
    sleep(0.5)
    print('|||         |||       |||         |||       |||            ')
    print('|||         |||       |||         |||       |||            ')
    sleep(0.5)
    print('|||         |||       |||         |||       |||            ')
    print('|||||||||||||||       |||||||||||||||       |||            ')
    sleep(0.5)
    print('|||||||||||||||       |||||||||||||||       |||            ')
    print('|||         |||       |||         |||       |||            ')
    sleep(0.5)
    print('|||         |||       |||         |||       |||            ')
    print('|||         |||       |||         |||       |||            ')
    sleep(0.5)
    print('|||         |||       |||         |||       |||            ')
    print('|||         |||       |||         |||       |||||||||||||||')
    print('\n\n')
    sleep(0.5)
    print('Seja bem vindo a calculadora, vamos começar?')
    sleep(1)


def separador():
    print('----------------------------------------------------------')


def obtencaoDosValores():
    valorEmDecimal1 = int(input("Insira o 1º valor:"), 2)
    sleep(0.3)
    print("...")
    valorEmDecimal2 = int(input("Agora insira o 2º valor:"), 2)
    sleep(0.5)
    separador()
    funcaoPrincipal(valorEmDecimal1, valorEmDecimal2)


def funcaoPrincipal(valor1, valor2):
    print("Qual operação você deseja realizar?\n\
        Digite + para somar \n\
        Digite * para multiplicação\n\
        Digite / para divisão\n\
        Digite s para sair")
    valorSelecionado = input("Insira o numero da operação desejada: ")
    if valorSelecionado == "+":
        print("O Resultado da soma", valor1 + valor2)
    elif valorSelecionado == "*":
        print("O Resultado da multiplicação: ",
              valor1 * valor2)
    elif valorSelecionado == "/":
        print("O Resultado da divisão: ", valor1 // valor2)
    elif valorSelecionado == "s":
        sleep(0.7)
        print('Até a próxima...')
        exit()
    else:
        print("""Você precisa selecionar uma das opções mostradas, vamos tentar
         novamente.""")
        sleep(0.6)
    funcaoPrincipal(valor1, valor2)


'''Funcao para validação dos caracteres digitados
def testeNumeros():
    nossaString = "ahah"
    for i in list(nossaString):
        if not i == "a":
            print('a')'''


funcaoEscritaInicial()
obtencaoDosValores()
