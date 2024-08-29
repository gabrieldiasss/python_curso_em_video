# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Digite um número: '))

dobro = n1 * 2
triplo = n1 * 3
raiz = n1**(1/2)

print('O dobro de {} vale {}'.format(n1, dobro))
print('O triplo de {} vale {}'.format(n1, triplo))
print('O dobro de {} vale {:.2f}'.format(n1, raiz))