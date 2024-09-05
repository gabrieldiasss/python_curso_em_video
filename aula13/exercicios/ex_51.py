#  Desenvolva um programa que leia o primeiro termo e a 
# razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

n1 = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
decimo = n1 + (20 - 1) * razao
for i in range(n1, decimo, razao):
    print('{}'.format(i), end=" -> ")
print("Acabou")
