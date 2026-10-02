for dado_A in range (1, 7):
    for dado_B in range (1, 7):
        if dado_A + dado_B != 7:
            continue #pula o que nao da 7

        print(f"{dado_A} + {dado_B} = 7")
    