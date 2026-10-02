#declaraçao de variaveis
numero: int = 0 
fatorial: int = 0
i: int = 0

#inicio
numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial = fatorial * i

print(f"O fatorial de {numero} é: {fatorial}")
#fimpara
#FIM