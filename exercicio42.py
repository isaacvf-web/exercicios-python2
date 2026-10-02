#var
i: int = 0
denominador: int = 0
S: float = 0.0

#inicio
for i in range (1, 50):
    denominador = (2 * i) - 1
    S = S + (i / denominador)
#fimpara
print("O valor final da soma da serie é: ", S)
    