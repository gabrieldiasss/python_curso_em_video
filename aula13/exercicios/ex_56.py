# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do 
# homem mais velho e quantas mulheres têm menos de 20 anos.


from datetime import date

nome_maior_idade = ''
maior = 0
soma_idade = 0
contador_menor_20 = 0

for i in range(1, 5):
    print('-----{}ª Pessoa -----'.format(i))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("[M/F]: "))

    if sexo == 'M' or sexo == 'F':

        soma_idade += idade

        if idade > maior and sexo == 'M':
            maior = idade
            nome_maior_idade = nome

        if idade <= 20:
            contador_menor_20 += 1
    else:
        print("ERRO!")

print("A média de idade do grupo é de {} anos".format(soma_idade/4))
print("O homem mais velho tem {} anos e se chama {}".format(maior, nome_maior_idade))
print("Ao todo são {} mulheres com menos de 20 anos".format(contador_menor_20))