# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input("Digite seu nome completo: ")

name_without_space = len(nome) - nome.count(' ')
split = nome.split()[0]

print('Seu nome em mauísculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))

print('1° forma - Seu nome tem ao todo {} letras (sem contar os espaços)'.format(name_without_space))
print('Seu primeiro nome é {} e ele tem {} letras'.format(split, len(split)))
