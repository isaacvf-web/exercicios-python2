#declaraçao de variaveis
numero: int = 0 
i: int = 0
soma: float = 1
fatorial: int = 1

#inicio
numero = int(input("Digite um numero N: "))

for i in range(1, numero + 1):
    fatorial = fatorial * i
    soma = soma + 1 / fatorial
print(f"A soma da série é: {soma}")
#fimpara
#fim