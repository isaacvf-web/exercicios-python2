##declaração de variaveis
casa: int = 0
quantidade: int = 1
total: int = 0

#inicio
for casa in range(1, 65):
    total = total + quantidade
    print(f"Casa {casa}: {quantidade} grãos")
    quantidade = quantidade * 2

print(f"Total de grãos no tabuleiro: {total}")
#fim