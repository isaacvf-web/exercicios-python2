#declaraçao de variaveis
A: int = 0

#inicio
A = int(input("Digite o valor de A: "))
if A % 2 == 0 and A % 3 == 0:
    print(f"O valor {A} é divisível por 2 e 3.")
else:
    print(f"O valor {A} não é divisível por 2 e 3.")
    #fimse
#FIM