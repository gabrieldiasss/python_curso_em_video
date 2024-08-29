# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira

import math

n1 = float(input("Digite um valor: "))

int = math.trunc(n1) # Dá pra usar o int() também!

print("O valor digitado foi {} e a sua porção inteira é {}".format(n1, int))