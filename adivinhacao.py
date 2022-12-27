#print("bah", "meo", sep="\n")
def jogar():
    import random

    print(29*"/")
    print("/   O Jogo da Adivinhação   / ")
    print(29*"/","\n")

    #numero_secreto = 5
    numero_secreto = round(random.randrange(1, 101))
    total_de_tentativas = 0
    #pontos = 1000
    rodada = 1
    #print(numero_secreto)

    print("Escolha a dificuldade")
    print("(1) Facil (2) Médio (3) Difícil")
    nivel = int(input("Digite o nível de dificuldade escolhido: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 1

    while (rodada <= total_de_tentativas):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Só é valido números de 1 a 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou!")
            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
        rodada = rodada +1

    #pontos_perdidos = numero_secreto - chute
    #pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__ == '__main__'):
    jogar()