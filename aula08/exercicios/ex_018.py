# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import tan, sin, cos, radians

angulo = float(input("Digite o angulo: "))

ang_convert = radians(angulo)

tangente = tan(ang_convert)
seno = sin(ang_convert)
cosseno = cos(ang_convert)

print("TANGENTE = {:.2f}\n SENO = {:.2f}\n COSSENO = {:.2f} ".format(tangente, seno, cosseno))

