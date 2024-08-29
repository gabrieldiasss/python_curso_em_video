# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

days = float(input("Quantos dias ele foi alugado? "))
km = float(input("Quantidade Km percorrido: "))

calcPerDays = days * 60 
calcKm = km * 0.15

print('Total ao pagar pelos dias {}'.format(calcPerDays))
print('Total ao pagar por KM rodado {}'.format(calcKm))
print('Total = R${:.2f}'.format(calcPerDays + calcKm))
