# Faça um programa que leia o comprimento do cateto 
# oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.


import math

oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento do cateto adjacente: "))

# 1° Forma - Usando funcionalidade hip da lib math

hip = math.hypot(oposto, adjacente)

print("1° Forma - O valor da hipotenusa é: {:.2f} ".format(hip))

# 2° Forma

c1 = math.pow(oposto, 2)
c2 = math.pow(adjacente, 2)

sum = c1 + c2

hip_2 = math.sqrt(sum) 

print("2° Forma - O valor da hipotenusa é: {:.2f} ".format(hip_2))

# 3° Forma

hip_3 = (oposto**2 + adjacente**2) ** (1/2)

print("2° Forma - O valor da hipotenusa é: {:.2f} ".format(hip_3))