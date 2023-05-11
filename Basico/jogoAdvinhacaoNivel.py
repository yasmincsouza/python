import random

print("*******************************")
print("Bem vindo ao jogo de advinhação")
print("*******************************", end="\n\n")

numero_secreto = random.randrange(1, 101) 
total_de_tentativas = 0

print("Qual o nível de dificuldade?")
print("(1) Fácil | (2) Médio | (3) Difícil")

nivel = int(input("Define o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(0, total_de_tentativas):
    print("### Tentativa {} de {} ###".format(rodada + 1, total_de_tentativas))
    chute_string = input("Digite um número entre 1 e 100: ")
    print("Você digitou", chute_string)
    chute = int(chute_string)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print(">>Você acertou!<<", end="\n\n")
        break 
    elif (maior):
        print(">>Você errou! O seu chute foi maior do que o numero secreto!<<", end="\n\n")
    elif(menor):
        print(">>Você errou! O seu chute foi menor do que o numero secreto!<<", end="\n\n")

print("Fim de jogo!")