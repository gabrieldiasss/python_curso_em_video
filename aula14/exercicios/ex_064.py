#  Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = 0
total = 0
count = 0
while n != 9999:

    n = int(input('Digite um número: '))

    if n != 9999:
        total += n

        count += 1

print('Você digitou {} números e a soma entre eles foi {}.'.format(count, total))