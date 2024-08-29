# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

price = float(input('Qual o preço do produto? R$'))

desc = price * (5 / 100) # ou já colocar direto 0.05
sub = price - desc

print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(price, sub))
