#declaraçao de variaveis
numero: int = 0
i: int = 0
resultado: int = 0

#inicio
numero = int(input("Digite um número:"))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
#fimpara
#FIM