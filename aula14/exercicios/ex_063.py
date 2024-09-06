# lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input("Termo: "))
razao =  int(input("Razão: "))

n = 1
quantidade_amostra = 10

while n < quantidade_amostra:
     
    print('{} -> '.format(termo), end='')

    termo += razao

    n += 1

    if n == quantidade_amostra:
        print('PAUSA')
        quantidade_amostra += int(input('\nQuantos termos você quer mostrar a mais? '))
    elif (quantidade_amostra == 0):
        break
print('Progressão finalizada com {} termos mostrados'.format(n))