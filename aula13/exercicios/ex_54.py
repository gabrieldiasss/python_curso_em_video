# Crie um programa que leia o ano de nascimento de sete pessoas.
#  No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0

ano_atual = date.today().year
for i in range(1, 7):
    year = int(input('Em que ano a {}° pessoa nasceu? '.format(i)))

    pessoa_idade = ano_atual - year

    if pessoa_idade < 18:
        menor += 1
    else:
        maior += 1

print("Ao todo tivemos {} pessoas maiores de idade".format(maior))
print("Ao todo tivemos {} pessoas menores de idade".format(menor))


