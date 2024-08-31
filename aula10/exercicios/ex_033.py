# faça um programa que leia três números e mostre qual é o maior e qual é o menor.


value1 = int(input("Primeiro valor: ")) 
value2 = int(input("Segundo valor: ")) 
value3 = int(input("Terceiro valor: ")) 

menor = 0
maior = 0

if value1 > value2 and value1 > value2 and value3 < value2:
    maior = value1
    menor = value3
if value2 > value1 and value2 > value3 and value3 < value1:
    maior = value2
    menor = value3
if value3 > value1 and value3 > value2 and value1 < value2:
    maior = value3
    menor = value1

print("O menor valor foi: {}".format(menor))
print("O maior valor foi: {}".format(maior))