# Faça um programa que leia um número qualquer e mostre o seu fatorial.

fatorial = int(input('Digite um número para calcular o fatorial: '))
contagem = fatorial
calc = 1
while contagem > 0:
    calc *= contagem 

    contagem -= 1

print('Calculando o total {}! '.format(calc))
