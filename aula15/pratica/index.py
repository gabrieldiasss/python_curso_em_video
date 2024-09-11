# INTERRONPENDO REPETIÇÕES WHILE

cont = 1
while True:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou') ### Nunca vai parar de executar esse programa

n = s = 0
while True:
    n = int(input('Digite um número'))

    if n == 9:
        break
    s += n
print(' A soma vale {}'.format(s))

