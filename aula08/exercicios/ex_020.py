# O mesmo professor do desafio 019 quer sortear a ordem de 
# apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import sample

aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")

alunos = [aluno1, aluno2, aluno3, aluno4]

print(sample(alunos))

