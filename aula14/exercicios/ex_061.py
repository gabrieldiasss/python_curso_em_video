# lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input("Termo: "))
razao =  int(input("Razão: "))

contagem = 0

calculo = termo

while contagem < 10:
    contagem += 1
    print('{}'.format(termo), end='')

    termo += razao
    
    print(' -> ', end='')

