# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida 
# o primeiro e o último nome separadamente.

name = input('Digite seu nome completo: ').strip()

break_name = name.split()

print("Muito prazer em te conhecer!")
print("Seu primeiro nome é: {}".format(break_name[0]))
print("Seu último nome é: {}".format(break_name[len(break_name) - 1]))