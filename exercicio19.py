#declaraçao de variaveis
A: int = 0
B: int = 0

#inicio
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
if A > B:
    print(f"O maior valor e: {A}")
elif B > A:
    print(f"O maior valor e: {B}")
else:
    print("Os valores sao iguais.")
    #fimse
#FIM