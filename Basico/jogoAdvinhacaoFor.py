print("*******************************")
print("Bem vindo ao jogo de advinhação")
print("*******************************", end="\n\n")

numero_secreto = 42
total_de_tentativas = 3

# range(start, stop, [step])
# Onde o step é opcional. Como queremos "pular" de 3 em 3, começando com 1 (start) até 10 (stop)
# for contador in range(1,11,3): 
#     print(contador)
for rodada in range(0, total_de_tentativas): # retorna um conjunto de números sequenciais
    print("### Tentativa {} de {} ###".format(rodada + 1, total_de_tentativas))
    chute_string = input("Digite um número entre 1 e 100: ")
    print("Você digitou", chute_string)
    chute = int(chute_string)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue # ele apenas sai da interação e volta pra proxima rodada 

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print(">>Você acertou!<<", end="\n\n")
        break # Ele para o For
    elif (maior):
        print(">>Você errou! O seu chute foi maior do que o numero secreto!<<", end="\n\n")
    elif(menor):
        print(">>Você errou! O seu chute foi menor do que o numero secreto!<<", end="\n\n")

print("Fim de jogo!")