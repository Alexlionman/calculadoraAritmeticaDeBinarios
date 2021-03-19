#Conversão de binário para inteiro int("numeroEmBinario", 2)

valorEmDecimal1 = int(input("Insira o valor:"), 2)
valorEmDecimal2 = int(input("Insira o valor:"), 2)
print("Escolha a operação: \n 1 - Soma \n 2 - Multiplicação \n 3 - Divisão")
valorSelecionado = input("Insira o numero da operação desejada: ")

if valorSelecionado == "1":
  print("Resultado da soma", valorEmDecimal1 + valorEmDecimal2)
elif valorSelecionado == "2":
    print("Resultado da multiplicação: ", valorEmDecimal1 * valorEmDecimal2)
elif valorSelecionado == "3":
    print("Resultado da divisão: ", valorEmDecimal1 // valorEmDecimal2)
else:
    print("Selecione uma das 3 opções")


