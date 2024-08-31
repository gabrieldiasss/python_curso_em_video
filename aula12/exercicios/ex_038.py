# 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print("O 1° número é maior")
elif n2 > n1:
    print("O 2° número é maior")
else:
    print("Eles são iguais")
