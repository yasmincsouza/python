print("*******************************")
print("Bem vindo ao jogo de advinhação")
print("*******************************", end="\n\n")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("### Tentativa {} de {} ###".format(rodada, total_de_tentativas))
    chute_string = input("Digite o seu numero: ")
    print("Você digitou", chute_string)
    chute = int(chute_string)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print(">>Você acertou!<<", end="\n\n")
    elif (maior):
        print(">>Você errou! O seu chute foi maior do que o numero secreto!<<", end="\n\n")
    elif(menor):
        print(">>Você errou! O seu chute foi menor do que o numero secreto!<<", end="\n\n")

    rodada = rodada + 1
print("Fim de jogo!")