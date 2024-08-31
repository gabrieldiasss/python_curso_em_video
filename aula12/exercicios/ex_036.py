# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Valor da casa: R$"))
salario = float(input('Salário do comprador: R$'))
financiamento = int(input("Quantos anos de financiamento? "))

meses = financiamento * 12
prestacao = valor_casa / meses
print("Para pagar uma casa de R${} em {} ano(s) a prestação será de R${:.2f} p/ mês".format(valor_casa, financiamento, prestacao))

porcentagem = salario * (30 / 100)

if prestacao > porcentagem: 
    print('Espréstimo negado')
else:
    print("Empréstimo CONCEDIDO")

