# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input("Distancia da viagem: "))

if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print("Você está prestes de começar uma viagem de {:.2f}km".format(dist))
print("E o preço da sua passagem será de R${:.2f}".format(preco))