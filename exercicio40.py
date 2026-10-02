#receber os limites do usuario
inicio = int(input("Digite o primeiro numero: "))
fim = int(input("Digite o segundo numero: "))

#garantir que o inicio seja menor que o fim (ajuste se necessário)
if inicio > fim:
   inicio, fim = fim, inicio

#percorrer o intervalo
for num in range(inicio, fim + 1):
    if num < 2:
        continue # Números menores que 2 não são primos
        
    e_primo = True
    
    # testar se o 'num' atual tem divisores
    for i in range(2, num):
        if num % i == 0:
            e_primo = False
            break # Se achou um divisor, para o laço interno
            
    # se a flag continuou True, exibe o numero
    if e_primo:
        print(num)
#fimpara
