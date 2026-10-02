soma = 0.0
i = 1

while i <= 15:
    numerador = i
    denominador = i ** 2  # Quadrado do numerador
    termo = numerador / denominador
    if i % 2 != 0:
        soma = soma + termo
    else:
        soma = soma - termo
        
    i = i + 1

print("O resultado da série é:", soma)