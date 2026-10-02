#declaraçao de variaveis
numero: int = 0
i: int = 0
anterior: int = 0
atual: int = 1
próximo: int = 0

#inicio
numero = int(input("Digite quantos termos deseja calcular: "))

print (anterior)
print (atual)

for i in range(2, numero):
    proximo = anterior + atual
    print (proximo)
    anterior = atual
    atual = proximo
    #fimpara
#fim