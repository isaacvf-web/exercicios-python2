#var
altura_ana: float = 1.10
altura_maria: float = 1.50
anos: int = 0

#inicio
while altura_ana <= altura_maria:
    altura_ana = altura_ana + 0.03
    altura_maria = altura_maria + 0.02
    anos = anos + 1

print("Para a Ana ultrapassar Maria em altura, serao necessarios: ", anos)