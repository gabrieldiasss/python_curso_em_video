### Módulos

# import NOME_DA_BIBLIOTECA => Pega todas as funcionalidade que a biblioteca tem disponível
# from NOME_DA_BIBLIOTECA import FUNCAO => pega aquela única funcjonalidade

# Math
    # ceil - Arredondar para cima
    # floor - Arredondar para baixo
    # trunc - Vai eliminar da virgula para frente
    # pow - Potencia
    # sqrt - Calcular a raiz quadrada
    # factorial - Calcular fatorial
from math import sqrt
 
num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num, raiz))