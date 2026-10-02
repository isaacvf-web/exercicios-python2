#declaraçao de variaveis
H_inicio: int = 0
H_fim: int = 0
M_inicio: int = 0
M_fim: int = 0
tempo_inicio: int = 0
tempo_fim: int = 0
tempo_jogo: int = 0

#inicio
H_inicio = int(input("Digite a hora de início do jogo: "))
M_inicio = int(input("Digite os minutos de início do jogo: "))
H_fim = int(input("Digite a hora de término do jogo: "))
M_fim = int(input("Digite os minutos de término do jogo: "))
tempo_inicio = H_inicio * 60 + M_inicio
tempo_fim = H_fim * 60 + M_fim
if tempo_fim >= tempo_inicio:
    tempo_jogo = tempo_fim - tempo_inicio
else:
    tempo_jogo = (tempo_fim - tempo_inicio) + 24 * 60
    #fimse
print(f"O jogo durou em minutos: {tempo_jogo} minutos.")
#fim