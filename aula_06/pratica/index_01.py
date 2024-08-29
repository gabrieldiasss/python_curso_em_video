n1 = str(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = float(input('Digite um valor: '))
n4 = bool(input('Digite um valor: '))

print(n1)
print(n2)
print(n3)
print(n4)

n = bool(input('Digite algo: '))

# isNumeric vai dizer se é possível converter um valor em um número
print(n.isnumeric()) # Saída: True ou False

# isalpha vai identficar se é uma letra
print(n.isalpha()) # Saída: True ou False

# isalnum vai identficar se é uma letra ou número
print(n.isalpha()) # Saída: True ou False

# isupper vai identficar se a letra está toda em MAIÚSCULA
print(n.isupper()) # Saída: True ou False