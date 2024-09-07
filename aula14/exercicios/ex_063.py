#  Escreva um programa que leia um número N inteiro qualquer e mostre na tela os
# N primeiros elementos de uma Sequência de Fibonacci. 

termos = int(input("Quantos termos você quer mostrar? "))

count = 0

first = 0
second = 1

next = 3

while count <= termos:

    next = first + second
    print('{}'.format(first, second, next))
    first = second
    second = next

    count += 1