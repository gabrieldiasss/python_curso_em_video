# Crie um programa que leia uma frase qualquer e diga se ela 
# é um palíndromo, desconsiderando os espaços.

frase = input("Digite a frase: ")

ao_contrario = list(frase)
ao_contrario.reverse()

separator = ''

juntar = separator.join(ao_contrario).upper()

print('O inverse de gustavo guanabara é: {}'.format(juntar.replace(' ', '')))
if frase == juntar:
    print('A frase digitada é palíndromo')
else:
    print('A frase digitada NÃO É palíndromo')