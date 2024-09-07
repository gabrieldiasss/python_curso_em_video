#  Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = 0
total = 0
count = 0

maior = 0
menor = 0

anterior = 0

next = 'S'
while next == 'S' or next == 's':

    anterior = n

    n = int(input('Digite um número: '))

    next = input('Quer continuar? [S/N] ')

    if n > anterior:
        maior = n
    if anterior < n:
        maior = n
    
    if anterior < n:
        menor = anterior
    if anterior > n:
        menor = n

    count += 1
    total += n
print('Você digitou {} números e a media foi {:.2f}.'.format(count, total / count))
print('Menor valor foi {} e o maior foi {}'.format(menor, maior))