#Faça um programa que calcule a soma entre todos os números que 
# são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma_3 = 0
quantidade = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        soma_3 = soma_3 + i
        quantidade = quantidade + 1
print('A soma de todos os {} valores solicitados é: {}'.format(quantidade, soma_3))