lado_esq = float(input("Primeiro segmento: "))
lado_dir = float(input("Segundo segmento: "))
base = float(input("Terceiro segmento: "))

lados = lado_esq + lado_dir

if lados > base:
    print("Os segmentos acima PODEM FORMAR triângulo!")
if lados <= base:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo!")



