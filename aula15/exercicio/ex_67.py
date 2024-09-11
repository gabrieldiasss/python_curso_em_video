# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo. 

while True:
    print('-'*10)
    n = int(input("Quer ver a tabuada de qual valor?: "))
    print('-'*10)

    if n < 0:
        break

    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
        i += 1

  

print(f'PROGRAMA TABUADA ENCERRADO. Volte sempre!')