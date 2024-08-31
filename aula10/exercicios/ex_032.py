# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

year = int(input("Digite algum ano, Se quiser coloque 0 para analisar o ano atual: "))

if year == 0:
    year =  date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("O ano {} é BISSEXTO".format(year))
else:
    print("O ano {} NÃO é BISSEXTO".format(year))
