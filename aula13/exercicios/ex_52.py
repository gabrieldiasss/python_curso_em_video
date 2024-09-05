# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

n = int(input("Digite um número: "))

count_div = 0
for i in range(1, n+1):
    if n % 1 == 0 and n % i == 0:
        count_div += 1
        print(count_div)
print('Ele é divísivel {} vezes!'.format(count_div))
if count_div == 2:
    print('Ele é PRIMO!')
else:
    print('Ele NÃO é PRIMO')