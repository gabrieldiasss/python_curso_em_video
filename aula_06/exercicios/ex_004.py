#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

write = (input('Digite qualquer coisa: '))

print(type(write))
print(write.isalnum())
print(write.isalpha())
print('ASCII', write.isascii())
print(write.isdecimal())
print(write.islower())
print('NUMERIC', write.isnumeric())
print(write.isspace())
print(write.isprintable())
print(write.isdigit())
print(write.istitle())
