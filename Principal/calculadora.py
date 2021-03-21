from time import sleep
import os

'''  
Usada para escrever as frases iniciais no console
'''


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

'''
Uma linha separadora usada para dividir algumas expressões
'''


def separador():
    print('----------------------------------------------------------')


'''
validador()
Valida que os caracteres digitados são binários, ou seja,
que contenham apenas "1" ou "0".
Se algum valor diferente de 0 ou 1 for encontrado, retorna falso
'''


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


'''
leitor()
Executa os dois primeiros inputs e recebe os valores digitados
como STRING.
Envia esses valores ao validador(), caso este retorne falso,
exibe uma mensagem ao usuário e reinicia o leitor()
Valida se o usuário apertou o enter sem digitar nada.
Ao final disso, envia os valores já formatados como decimais
para a funcaoPrincipal()
'''


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


'''
finalizar()
Método executado toda vez que o usuário solicita a finalização
da aplicação. Isso pode ocorrer pelo continuar() ou
funcaoPrincipal()
Exibe uma mensagem com intervalos de tempo sleep()
e encerra a execução do programa
'''


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


'''
continuar()
Solicita ao usuario a confirmação de continuação
caso receba "1", limpa o console e executa o leitor()
caso receba "2", executa o finalizaR()
'''


def continuar():
    print('Quer realizar outra operação? \n1 - Sim \n2 - Não')
    outraOperacao = input('')
    if outraOperacao == '1':
        os.system('cls') or None
        leitor()
    elif outraOperacao == '2':
        finalizar()
    else:
        print("Digite um valor válido...")
        sleep(1.2)
        print("Tentando novamente")
        sleep(1.2)
        separador()
        continuar()


'''
funcaoPrincipal
rebebe dois valores no formato decimal
*Solicita ao usuário a operação desejada
**Le o valor inserido pelo usuário, caso inválido executa novamente
***Verifica que o valor inserido é valido
****Mostra o resultado da operação de acordo com o valor selecionado
*****Ao final de qualquer operação, executa o continuar()
'''


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
