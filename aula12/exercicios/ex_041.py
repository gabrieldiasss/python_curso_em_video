# A Confederação Nacional de Natação precisa de um programa que leia o ano de 
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
from datetime import date

ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento

print("O atleta tem {} anos".format(idade))

if idade <= 8:
    print("Classificação: PRÉ MIRIM")
elif idade > 8 and idade <= 10:
    print("Classificação: MIRIM")
elif idade > 10 and idade <= 12:
    print("Classificação: PETIZ")
elif idade > 12 and idade <= 14:
    print("Classificação: INFANTIL")
elif idade > 14 and idade <= 16:
    print("Classificação: JUVENIL")
elif idade > 16 and idade <= 19:
    print("Classificação: JUNIOR")
else:
    print("Classificação: SÊNIOR")
    