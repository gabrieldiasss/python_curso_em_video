# CONDIÇÕES ANINHADAS

nome = str(input('Qual é seu nome? '))

if nome == "Gabriel Dias":
    print("Que nome bonito!")
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print("Seu nome é muito popular no Brasil!")
else:
    print("Que nome normal!")
print('Tenha um bom dia {}'.format(nome))