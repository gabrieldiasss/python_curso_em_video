# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

city = input('Em qual cidade você nasceu? ')

validate = city.strip().upper()

print("SANTO" == validate.split()[0])