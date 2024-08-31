# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual é o salario? "))

if salario <= 1250:
    aumento = salario * (15 / 100)
    total = salario + aumento
else:
    aumento = salario * (10 / 100)
    total = salario + aumento

print("Quem ganahava R${} passa a ganhar R${} agora.".format(salario, total))