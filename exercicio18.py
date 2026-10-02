#declaraçao de variaveis
A: int = 0
B: int = 0
Diferenca: int = 0

#inicio
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
if A > B:
    Diferenca = A - B
else:
    Diferenca = B - A
print(f"A diferença entre A e B é: {Diferenca}")
#FIM