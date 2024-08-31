# Manipulando Texto

# Todo texto está em aspas simples ou aspas duplas
# Python vai criar mini espaços dentro da memório do computador, cada 1 desse mini espaço vai colocar cada uma das letras

frase = 'Curso em Vídeo Python' # 21 caracteres ao total

## Operações com stirng

# Fatiamento

print(frase[9])

# do 9 até o 13 - Porém exclui o 13
print(frase[9:13])
print(frase[9:21])

# do 9 até o 21 e pulando de 2 em 2 
print(frase[9:21:2])

# Quando omitimos o ínicio ele começa do caractere 0
print(frase[:5])

# Quando omitimos o final ele começa do último caractere
print(frase[15:])

# Vai começar do 9 e vai até o final, pulando de 3 em 3
print(frase[9::3])

# Ánalise

# Quantidade de caractere
print(len(frase))

# Quantidade da letra O
print(frase.count('o'))

# Quantidade da letra O do 0 até o 13
print(frase.count('o'))

# Retorna em que indice começa a palavra que você colocou
print('FIND =', frase.find('o'))

# Se não encontra a string que vc colocou retorna -1
print('FIND =', frase.find('Gabriel'))

# Operador In, vai conferir se existe a palavra
print('Curso' in frase)

## Transformação

# Substituir a palavra Python por android
print(frase.replace('Python', 'Android'))

# Deixar tudo em letra maiúscuça
print(frase.upper())

# Deixa tudo em minusculo
print(frase.lower())

# Só o primeiro caractere da string vai ficar em Maiuscula
print(frase.capitalize())

# O primeiro caractere de toda palavra da string vai ficar em maiuscula
print(frase.title())

frase_1 = '   Aprenda Python   '

# Vai remover todos os espaços do início e fim
print(frase_1.strip())

# Vai remover os últimos espaços (da direita)
print(frase_1.rstrip())

# Vai remover os primeiros espaços (da esquerda)
print(frase_1.lstrip())

## Divisão

# Cada palavra é colocado em uma outra lista e irá recomeçar o indice do 0 - [Curso] [em] [Vídeo] [Python]
print(frase.split())

# Juntar a frase que está "splitada" adicionando separador -
print('-'.join(frase))