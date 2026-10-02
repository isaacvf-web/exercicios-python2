#declaraçao de variaveis
numero: int = 0
soma: float = 0.0
i: int = 0

#inicio
numero = int(input("Digite um número N: "))

for i in range(1, numero + 1):
    soma = soma + i

print(f"A soma dos números de 1 até {numero} é: {soma}")
#fimpara
#FIM