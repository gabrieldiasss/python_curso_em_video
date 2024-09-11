# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

quantity_age = 0
quantity_mens = 0
quantity_woman = 0

while True:
    print('-'*15)
    print("Cadastre uma pessoa")
    print('-'*15)

    if next == 'N':
        break

    age = int(input('Idade: '))
    sex = input('Sexo? [M/F] ').upper()

    print('-'*15)

    next = input('Quer continuar? [S/N] ').upper()

    if age > 18:
        quantity_age += 1

    if sex == 'F' and age <= 19:
        quantity_woman += 1

    if sex == 'M':
        quantity_mens += 1

    if next != 'S':
        break

print(f'O total de pessoas com mais de 18 anos: {quantity_age}')
print(f'Ao todo temos {quantity_mens} homens cadastrados')
print(f'E temos {quantity_woman} mulheres com menos de 20 anos')