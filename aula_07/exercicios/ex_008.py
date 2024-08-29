# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = int(input("Uma distância em metros: "))

print('A medida de {:.1f} corresponde a:'.format(metros))
print(metros / 1000,'km')
print(metros / 100,'hm')
print(metros / 10,'dam')
print(metros * 10,'dm')
print(metros * 100,'cm')
print(metros * 1000,'mm')