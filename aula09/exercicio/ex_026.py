# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a 
# primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase: ')

validate = frase.strip().upper()

print('A letra A aparece {} vezes na frase.'.format(validate.count('A')))
print('A primeira letra A apareceu na posição {}'.format(validate.find('A') + 1))
print('A última letra A apareceu na posição {}'.format(validate.rfind('A') + 1))
