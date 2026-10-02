#declaraçao de variaveis
A: int = 0
B: int = 0

#inicio
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
if A > B:
    if A % B == 0:
        print(f"O valor {A} é múltiplo de {B}.")
    else:
        print(f"O valor {A} não é múltiplo de {B}.")
        #fimse
else:
    if B % A == 0:
        print(f"O valor {B} é múltiplo de {A}.")
    else:
        print(f"O valor {B} não é múltiplo de {A}.")
        #fimse
#FIM