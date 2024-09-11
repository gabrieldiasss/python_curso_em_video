# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

print('-'*15)
print("Cadastre uma LOJA SUPER BARATÃO")
print('-'*15)

total = 0
maior = 0
barato = 0

anterior = 0

while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$'))

    print('-'*15)



    total += preco

    if preco > 1000:
        maior += 1

    if anterior < preco:
        menor = anterior
        produto_barato = nome
    if anterior > preco:
        menor = preco
        produto_barato = nome

    next = input('Quer continuar? [S/N] ').upper()

    if next != 'S':
        break
print(f'O total da compra foi: R${total:.2f}')
print(f'Temos {maior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R${menor:.2f}')