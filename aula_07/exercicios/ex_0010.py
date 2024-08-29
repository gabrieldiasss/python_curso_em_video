# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

money = float(input("Quando você tem na carteira? R$"))

dolar = money / 5.56

print("Com R${} você pode comprar U${:.2f}".format(money, dolar))