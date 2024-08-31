# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário 
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input("Digite um número inteiro: "))

print("Escolha uma das bases para a conversao: \n [ 1 ] Converter para BINÁRIO \n [ 2 ] Converter paqra OCTAL \n [ 3 ] Converter para Hexadecimal")

option = int(input("Sua opção: "))

if option == 1:
    print("{} Convertido para BINÁRIO é igual a {}".format(n, bin(n)[2:]))
elif option == 2:
    print("{} Convertido para OCTAL é igual a {}".format(n, oct(n)[2:]))
elif option == 3:
    print("{} Convertido para HEXADECIMAL é igual a {}".format(n, hex(n)[2:]))
else:
    print("Opção inválida. Tente novamente")
