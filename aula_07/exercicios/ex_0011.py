# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

width = float(input('Largura da parede: '))
height = float(input('Altura da parede: '))

area = width * height
litros = area / 2

print('Sua parade tem a dimensão de {}x{} e sua área é de {}m²'.format(width, height, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(litros))
