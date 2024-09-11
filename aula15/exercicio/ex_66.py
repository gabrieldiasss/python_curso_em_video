# Crie um programa que leia números inteiros pelo teclado. O programa só vai 
# parar quando o usuário digitar o valor 999, que é a condição de parada. No final, 
# mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

n = count = total = 0

while n != 999:
    n = int(input("Digite um valor (999 parar): "))

    if n == 999:
        break

    total += n

    count += 1 


print(f'A soma dos {count} valores foi {total}!')