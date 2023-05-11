import forca
import jogoAdvinhacaoPontuacao

def escolhe_jogo():
    print("********************************")
    print("*******Escolha o seu jogo*******")
    print("********************************", end="\n\n")

    print("(1) Forca | (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("jogando Adivinhação")
        jogoAdvinhacaoPontuacao.jogar()
        
    print("Fim de jogo!")

if (__name__ == "__main__"): # Le o arquivo principal e roda ele
    jogar() 