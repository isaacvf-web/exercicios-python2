#declaraçao de variaveis
A: float = 0
B: float = 0
C: float = 0

#inicio
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
delta = (B ** 2) - (4 * A * C)
if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    raiz = -B / (2 * A)
    print(f"Existe uma raiz real: {raiz}")
else:
    raiz1 = (-B + (delta ** 0.5)) / (2 * A)
    raiz2 = (-B - (delta ** 0.5)) / (2 * A)
    print(f"Existem duas raízes reais: {raiz1} e {raiz2}")
    #fimse
#FIM