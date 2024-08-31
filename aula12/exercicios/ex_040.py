# Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2

print("Tirando {} e {}, a média do aluno é {}".format(n1, n2, media))

if media >= 7:
    print("Aluno APROVADO")
elif media > 4 and media < 7:
    print("Recuperação")
else:
    print("Aluno Reprovado")
