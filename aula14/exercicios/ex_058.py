# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print("Sou seu computador...")
print("Acabei de pensar em um número ente 0 e 10.")
print("Será que você consegue adivinhar qual foi?")

resposta = int(input("Qual é seu palpite? "))
pc = randint(0, 10)
tentativas = 1

while resposta != pc:
    menosOuMais = 'Mais...' if pc > resposta else 'Menos...'
    resposta = int(input('{} Tente mais uma vez: '.format(menosOuMais)))
    tentativas += 1

print('Acertou com {} tentativas. Parabéns'.format(tentativas))
print('Eu pensei no número: {}.'.format(pc))