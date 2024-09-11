# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('-'*15)
print("Banco do Curso em Vídeo")
print('-'*15)

saque = int(input('Digite o valor que deseja sacar: R$ '))
n50 = n20 = n10 = n1 = 0

while True:
    if saque >= 50:
        saque -= 50
        n50 += 1
    else:
        if saque >= 20:
            saque -= 20
            n20 += 1
        else:
            if saque >= 10:
                saque -= 10
                n10 += 1
            else:
                if saque >= 1:
                    saque -= 1
                    n1 += 1
    if saque == 0:
        break
print(f'Você receberá {n50} notas de R$50, {n20} de R$20, {n10} de R$10 e {n1} de R$1.')