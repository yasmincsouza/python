print("*******************************")
print("Bem vindo ao jogo de advinhação")
print("*******************************", end="\n\n")

numero_secreto = 42

# Recebe os dados  
# A função input sempre retorna um texto (string)
chute_string = input("Digite o seu numero: ")
print("Você digitou:", chute_string)
chute = int(chute_string) # Python não converte os tipos automaticamente. É necessario fazer a conversão manual

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

# Em python você indica que é para ler o if else depois de :
if (acertou):
    print(">>Você acertou!<<", end="\n\n")
elif (maior):
    print(">>Você errou! O seu chute foi maior do que o numero secreto!<<", end="\n\n")
elif(menor): #forma de escrever o else if em >>python<<
    print(">>Você errou! O seu chute foi menor do que o numero secreto!<<", end="\n\n")

print("Fim de jogo!")