# Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for i in range(1, 6):
    
    p = float(input('Peso da {}° pessoa: '.format(i)))

    if p>maior:
        maior = p
    if p<menor:
        menor = p
print(f'Dentre esses, o maior peso foi {maior}kg e o menor foi {menor}kg ')