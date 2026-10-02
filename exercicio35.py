##declaraçao de variaveis
num1: int = 0
num2: int = 0
maior: int = 0
menor: int = 0
i: int = 0
soma: int = 0

#inicio
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: ")) 
if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1
    print(f"O maior número é: {maior}")
#fimse
for i in range(menor, maior + 1):
        if i % 2 != 0:
            soma = soma + i
print (f"A soma dos números impares entre {menor} e {maior} é: {soma}")
#fimpara
#fim