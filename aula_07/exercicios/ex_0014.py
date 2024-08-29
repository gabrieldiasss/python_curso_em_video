# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Digite o °C "))
fahrenheit = (celsius * (9/5)) + 32

print('A temperatura de {}°C corresponde a {}°F!'.format(celsius, fahrenheit))