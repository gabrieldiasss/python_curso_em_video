#Escreva um programa que faça o computador "pensar" em um número inteiro 
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
import time

n = int(input("Em que número eu pensei? "))

n_machine = randint(0, 5)

print("Processando...")
time.sleep(3)

if n == n_machine:
    print("Parabéns! Você conseguiu me vencer")
else:
    print('GANHEI! Eu pensei no número {} não no {}'.format(n_machine, n))