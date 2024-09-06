# Crie um programa que leia dois valores e mostre um menu na tela:
from time import sleep
option = 0

while option != 5:
    if option != 4:
        n1 = int(input("Digite o 1° valor: "))
        n2 = int(input("Digite o 2° valor: "))

    print(" [ 1 ] Somar \n [ 2 ] Multiplcar \n [ 3 ] Maior \n [ 4 ] Novos números \n [ 5 ] Sair do programa ")

    option = int(input('>'*5 + ' Qual é sua opção? '))

    if option == 1:
        s = n1 + n2
        print('A soma entre {} e {} é: {}'.format(n1, n2, s))
        print('=-'*10)
    elif option == 2:
        m = n1 * n2
        print('A multiplicação entre {} e {} é: {}'.format(n1, n2, m))
        print('=-'*10)
    elif option == 3:
        maior = 0

        if n1 > n2:
            maior = n1
        if n2 > n1:
            maior = n2
        
        print('O número maior entre {} e {} é o: {}'.format(n1, n2, maior))
        print('=-'*10)
    elif option == 4:
        print('Informe os números novamente: ')
        n1 = int(input("Digite o 1° valor: "))
        n2 = int(input("Digite o 2° valor: "))

        print('-'*10)
    elif option == 5:
        #sair do programa
        print('Finalizando...')
        sleep(1)
    else:
        print("Essa opção não existe. Tente novamente")

print("Fim do programa! Volte sempre")