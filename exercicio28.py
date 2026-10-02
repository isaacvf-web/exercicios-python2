#declaraçao de variaveis
venda_mensal: float = 0.0
preço_atual: float = 0.0
novo_preço: float = 0.0

#inicio
venda_mensal = float(input("Digite o valor da venda mensal: "))
preço_atual = float(input("Digite o valor do preço atual: "))
if venda_mensal <500 and preço_atual < 30:
    novo_preço = preço_atual * 1.10
    print(f"O novo preço é: {novo_preço:.2f}.")
elif venda_mensal >= 500 and venda_mensal < 1000 and preço_atual >= 30 and preço_atual < 80:
    novo_preço = preço_atual * 1.15
    print(f"O novo preço é: {novo_preço:.2f}.")
elif venda_mensal >= 1000 and preço_atual >= 80:
    novo_preço = preço_atual * 0.95
    print(f"O novo preço é: {novo_preço:.2f}.")
else:
    print("Não há alteração no preço.")
    #fimse
#FIM