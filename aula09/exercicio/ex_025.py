# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = input('Digite seu nome completo: ')

validate = name.strip().upper()

print("SILVA" in validate)