# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

price = float(input("Preço das compras: R$"))
print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista dinheiro/cheque \n[ 2 ] à vista cartão \n[ 3 ] 2x no cartão \n[ 4 ] 3x ou mais no cartão" )

option = float(input('Qual é a opção? '))

if option == 1:
    desc = price * (10 /100)
    print("Sua compra de R${} vai custar R${}".format(price, price - desc))
elif option == 2:
    desc = price * (5 /100)
    print("Sua compra de R${} vai custar R${}".format(price, price - desc))
if option == 3:
    print("Com essa forma de pagamento você não pussui nenhum desconto, portanto o preço final será {}".format(price))
elif option == 4:
    installments = int(input('Quantas parcelas? '))
    fees = price * (20 / 100)
    installments_per_month = fees / installments 
    price_with_fees = (price / installments) + installments_per_month

    print("Sua compra será parcelada em {}x de R${} COM JUROS".format(installments, price_with_fees))
    print("De R${} sua compra vai custar no final R${}".format(price, price + fees))
else: 
    print("Opção inválida, tente novamente.")