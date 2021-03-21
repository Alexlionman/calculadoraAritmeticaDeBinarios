from time import sleep
import os


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
    print('|||         |||  ||   |||         |||  ||   |||||||||||||||')
    print('\n\n')
    sleep(0.5)
    print('Seja bem vindo a calculadora, vamos começar?')
    sleep(1)
    print('...Iniciando...')
    sleep(1)
    print('...')
    sleep(0.7)
    print('...')
    sleep(1)


def separador():
    print('----------------------------------------------------------')


def validador(valoreInseridos):
    existeValorNaoBinario = True
    for i in list(valoreInseridos):
        if i != '1' and i != '0':
            existeValorNaoBinario = False
            break
    if not existeValorNaoBinario:
        print('Um valor não binário foi inserido, digite somente 0 ou 1')
        sleep(1.4)
        print('Tentando novamente...')
        sleep(1.9)
    return existeValorNaoBinario


def leitor():
    os.system('cls') or None
    print('Vamos lá')
    separador()
    primeiroValorString = input("Insira o 1º valor:  ")
    if primeiroValorString == '':
        print("Você digitou um valor invalido.")
        sleep(1.3)
        print('Tentando novamente')
        sleep(1.0)
        leitor()
    segundoValorString = input("Agora insira o 2º valor:  ")
    if segundoValorString == '':
        print("Você digitou um valor invalido.")
        sleep(1.3)
        print('Tentando novamente')
        sleep(1.0)
        leitor()
    valoresEmConjunto = primeiroValorString+segundoValorString
    if validador(valoresEmConjunto):
        sleep(0.3)
        print("...")
        valorEmDecimal1 = int((primeiroValorString), 2)
        valorEmDecimal2 = int((segundoValorString), 2)
        sleep(0.5)
        separador()
        funcaoPrincipal(valorEmDecimal1, valorEmDecimal2)
    else:
        leitor()


def finalizar():
    os.system('cls') or None
    sleep(0.5)
    print('Obrigado por usar nossa aplicação')
    separador()
    sleep(1.5)
    print('Até a próxima...')
    sleep(1.5)
    separador()
    sleep(1.5)
    print('---CALCULADORA DE BINÁRIOS© Todos os direitos reservados---')
    print('Desenvolvido com <3 por Alex, Ana Caroline & Carol')
    exit()


def continuar():
    print('Quer realizar outra operação? \n1 - Sim \n2 - Não')
    outraOperacao = input('')
    if outraOperacao == '1':
        os.system('cls') or None
        leitor()
    else:
        finalizar()


def funcaoPrincipal(valor1, valor2):
    print("Qual operação você deseja realizar?\n\
        Digite + para somar \n\
        Digite * para multiplicação\n\
        Digite / para divisão\n\
        Digite t para ver todos os resultados\n\
        Digite s para sair")
    valorSelecionado = input("Insira o caracter da operação desejada: ")
    if valorSelecionado == "+":
        print("A soma de ", valor1, "+", valor2, "é: ", valor1 + valor2)
        sleep(0.5)
        separador()
        continuar()
    elif valorSelecionado == "*":
        print("A multiplicação de ", valor1, "*",
              valor2, "é: ", valor1 * valor2)
        sleep(0.5)
        separador()
        continuar()
    elif valorSelecionado == "/":
        print("A divisão de ", valor1, "/", valor2, "é: ", valor1 / valor2)
        sleep(0.5)
        separador()
        continuar()
    elif valorSelecionado == 't':
        print('Todos os resultados: ')
        print("A soma de ", valor1, "+", valor2, "é: ", valor1 + valor2)
        print("A multiplicação de ", valor1, "*",
              valor2, "é: ", valor1 * valor2)
        print("A divisão de ", valor1, "/", valor2, "é: ", valor1 / valor2)
        sleep(0.5)
        separador()
        continuar()
    elif valorSelecionado == "s":
        sleep(0.7)
        finalizar()
    else:
        print("""Você precisa selecionar uma das opções mostradas, vamos tentar
         novamente.""")
        sleep(2.6)
        print('...Reiniciando...')
        sleep(1.4)
        print('...')
        sleep(1.0)
        os.system('cls') or None
        funcaoPrincipal(valor1, valor2)


'#Inicio da execução'
funcaoEscritaInicial()
leitor()
