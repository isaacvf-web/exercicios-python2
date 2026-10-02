#declaraçao de variaveis
N1: float = 0
N2: float = 0
N3: float = 0
N4: float = 0

#inicio
N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))
N4 = float(input("Digite a quarta nota: "))
media = (N1 + N2 + N3 + N4) / 4
if media >= 6.0:
    print(f"A média é: {media}. APROVADO.")
elif media >= 3.0 and media < 6.0:
    print(f"A média é: {media}. EXAME.")
else:
    print(f"A média é: {media}. REPROVADO.")
    #fimse
#FIM