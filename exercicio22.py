#declaraçao de variaveis
A: int = 0
B: int = 0

#inicio
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
if A > B:
    print(f"os valores em ordem crescente são: {B}, {A}.")
elif A < B:
    print(f"os valores em ordem crescente são: {A}, {B}.")
else:
    print("Os valores são iguais.")
    #fimse
#FIM