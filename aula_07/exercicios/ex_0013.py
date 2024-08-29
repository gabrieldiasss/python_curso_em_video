# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

money = float(input('Qual o salário de um funcionário? R$'))

promo = money * (15 / 100)
aum = money + promo
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(money, aum))