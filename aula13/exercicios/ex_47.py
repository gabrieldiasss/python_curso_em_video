# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# Mais processamento
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')
print('Acabou!')

# Menos processamento
for i in range(1, 51, 2):
    print(i, end=' ')
print('Acabou!')