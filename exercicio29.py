#declaraçao de variaveis
tipo: int = 0
valor: float = 0.0
rendimento: float = 0.0
valor_total: float = 0.0

#inicio
tipo = int(input("Digite o tipo de investimento (1 - Poupança, 2 - Renda Fixa): "))
valor = float(input("Digite o valor do investimento: "))
if tipo == 1:
    rendimento = valor * 0.03
    valor_total = valor + rendimento
    print(f"O valor total do investimento é: {valor_total:.2f}.")
elif tipo == 2:
    rendimento = valor * 0.05
    valor_total = valor + rendimento
    print(f"O valor total do investimento é: {valor_total:.2f}.")
else:
    print("Tipo de investimento inválido.")
    #fimse
#FIM