#declaraçao de variaveis
A: int = 0
B: int = 0
C: int = 0
D: int = 0

#inicio
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))
if D<A:
    print(f"os valores em ordem crescente são: {D}, {A}, {B}, {C}.")
elif D<B:
    print(f"os valores em ordem crescente são: {A}, {D}, {B}, {C}.")
elif D<C:
    print(f"os valores em ordem crescente são: {A}, {B}, {D}, {C}.")
else:
    print(f"os valores em ordem crescente são: {A}, {B}, {C}, {D}.")
    #fimse
#FIM