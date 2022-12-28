def jogar():
    import random

    print(25*"/")
    print("/   O Jogo da Forca     / ")
    print(25*"/","\n")

    arquivo = open("palavras.txt" , "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras [numero].upper()

    #print(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    #palavra_secreta = "topper".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    while(not enforcou and not acertou):
        
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    #print("Encontrei a letra {} na posição {}" .format(letra, index))
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            desenha_forca(erros)
        
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou, joga mt krl")
    else:
        print("Você errou, a palavra era",(palavra_secreta))
        #print(palavra_secreta)

    #print(letras_acertadas)

    #print("Fim do jogo")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == '__main__'):
    jogar()