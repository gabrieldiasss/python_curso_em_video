### Condicionais

time = int(input('Quantos anos tem seu carro?'))

if time <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

print('carro ono' if time <= 3 else 'carro velho')