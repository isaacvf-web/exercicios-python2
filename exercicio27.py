#declaraçao de variaveis
voltas: int = 0
extensao: int = 0
tempo: int = 0
dist_km: float = 0.0
tempo_h: float = 0.0
vel_media: float = 0.0

#inicio
voltas = int(input("Digite o número de voltas: "))
extensao = int(input("Digite a extensão da pista em metros: "))
tempo = int(input("Digite o tempo gasto em segundos: "))
if tempo >0:
    dist_km = (voltas * extensao) / 1000
    tempo_h = tempo / 3600
    vel_media = dist_km / tempo_h
    print(f"A velocidade média do carro é: {vel_media:.2f} km/h.")
else:
    print("O tempo deve ser maior que zero.")
    #fimse
#FIM