def jogar():
    print("********************************")
    print("***Bem vindo ao jogo de Forca***")
    print("********************************", end="\n\n")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"] #Lista
    
    enforcou = False
    acertou = False

    print(letras_acertadas)
    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip() 

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra #colocando o valor na lista de acordo com o index
            index = index + 1
        print(letras_acertadas)

    print("Fim de jogo!")

if (__name__ == "__main__"): 
    jogar() 