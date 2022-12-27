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

    #print(palavras)

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
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou, joga mt krl")
    else:
        print("Mas tu é ruim pra krl em")
    print("Fim do jooj")

    #print(letras_acertadas)

    #print("Fim do jogo")

if(__name__ == '__main__'):
    jogar()