import forca
import adivinhacao

print("***********************")
print("* Escolha o seu jojo! *")
print("***********************")

while input == 0 or 3:

    print("(1) Adivinhação (2) Forca")
    jogo = int(input("Qual jojo? "))

    if(jogo == 1):
        print ("Jojando Adivinhação")
        adivinhacao.jogar()
    elif(jogo == 2):
        print ("Jojando Forca")
        forca.jogar()
    else:
        print("Escolha inválida")