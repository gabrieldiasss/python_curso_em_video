n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
m = n1 * n2
e = n1 ** n2

# End junta os 2 prints
# \n quebra a linha
# {:.3f} Formata para 3 casas deciamis

print('A soma é {}, \n o produto é {} \n divisão é {:.3f}'.format(s, m, d), end='>>>')
print('Divisão inteira é {}, potencia é {}'.format(di, e))

