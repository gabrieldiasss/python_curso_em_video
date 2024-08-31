# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input("Qual é a velocidade atual do carro? "))

if v >= 80:
    print("MULTADO! Você excedeu o limite permitido que é de 80km/h")
    multa = (v - 80) * 7
    print("Você deve pagar uma multa de R${:.2f}".format(multa))
print('Tenha um bom dia, dirija com segurança!')