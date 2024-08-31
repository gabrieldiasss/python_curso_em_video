# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua 
# idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do 
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento

print("Quem nasceu em {} tem {} anos em {}".format(ano_nascimento, idade, ano_atual))

if idade == 18:
    print("Você deve se alistar ao serviço militar AGORA!")
elif idade < 18:
    diferenca = 18 - idade 
    print("Ainda falta {} anos para o alistamento".format(idade - 18))
    print("Seu alistamento será em {}".format(ano_atual + diferenca))
else:
    print("Você já deveria ter se alistado há {} ano(s)".format(idade - 18))
    print("Seu alistameto foi em {}".format(ano_nascimento + 18))