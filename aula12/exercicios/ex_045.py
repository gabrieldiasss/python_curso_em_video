# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
print(" Sua opções: \n[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA")

play = int(input("Qual é a sua jogada? "))
machine = randint(0, 2)


print("JOGADOR escolheu: ", play)
print("COMPUTADOR escolheu: ", machine)

if play == 0 and machine == 2 or play == 1 and machine == 0 or play == 2 and machine == 1:
    print("JOGADOR VENCEU")
elif machine == 0 and play == 2 or machine == 1 and play == 0 or machine == 2 and play == 1:
    print("COMPUTADOR VENCEU")
else:
    print("Empate. Jogue novamente!")