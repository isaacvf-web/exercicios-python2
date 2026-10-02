base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1
i = 0

while i < expoente:
    resultado = resultado * base
    i = i + 1

print(f"O resultado da potenciação é: {resultado}")
