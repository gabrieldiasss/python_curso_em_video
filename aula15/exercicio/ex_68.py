# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint

print('-='*15)
print("Vamos jogar par ou ímpar")
print('-='*15)

wins = 0

while True:
    pc = randint(0, 10)

    vc = int(input('Diga um valor: '))
    parOuImpar = input('Par ou Ímpar? [P/I] ').upper()

    s = vc + pc

    if s % 2 == 0:
        res = "PAR"
    else:
        res = "ÍMPAR"

    print('-'*15)
    print(f'Você jogou {vc} e o computador {pc}. Total de {s} deu {res}')
    print('-'*15)

    if parOuImpar == 'P' and res == 'PAR':
        print('VOCÊ VENCEU! Parabéns')
        print('Vamos jogar novamente...')
        print('-='*15)

        wins += 1
    elif parOuImpar == 'I' and res == 'ÍMPAR':
        print('VOCÊ VENCEU! Parabéns')
        print('Vamos jogar novamente...')
        print('-='*15)

        wins += 1
    else:
        break

print(f'GAME OVER! Você venceu {wins} vezes')