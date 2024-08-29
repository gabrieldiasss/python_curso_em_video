# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite anota da 1° prova: '))
nota2 = float(input('Digite anota da 2° prova: '))

media = (nota1 + nota2) / 2

print('A média entre {} e {}: é {}'.format(nota1, nota2, media))