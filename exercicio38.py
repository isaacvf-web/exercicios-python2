##declaração de variaveis
numero: float = 0
i: int = 0
maior: float = 0
menor: float = 0

#inicio
for i in range(1, 101):
    numero = float(input(f"Digite o {i}º número: "))
    if numero > 0:
        if numero > maior:
            maior = numero
        if menor == 0 or numero < menor:
            menor = numero

print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")
#fim