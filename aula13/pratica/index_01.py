# Podemos passar uma variável de número para o for

n = int(input("Digite um número: "))

for i in range(0, n+1):
    print(i)
print('FIM')

# colocando mais variáveis
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for i in range(i, f+1, p):
    print(i)
print('FIM')

