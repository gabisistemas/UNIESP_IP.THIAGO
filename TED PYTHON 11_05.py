import random

numero_sorteado = random.randrange(1,100)
total_de_tentativas = 0

print()
print("+ . " * 20)
print("OLÁ! SEJA BEM VINDO! QUE TAL SE DIVERTIR UM POUCO? VAMOS COMEÇAR NOSSO JOGO?")
print("+ . " * 20)
print("\nNº 1. NESTE JOGO VOCÊ PRECISA ADIVINHAR QUAL NÚMERO EU ESCOLHI, OS VALORES VÁLIDOS ESTÃO ENTRE 01 E 100.")
print("Nº 2. VAMOS DEFINIR O NÍVEL DE DIFICULDADE QUE VOCÊ ENFRENTARÁ.")

while(True):

    dificuldade = int(input("\n \nO QUÃO VOCÊ SE GARANTE NO NOSSO JOGO? \n(1)ESTOU NERVOSO... \n(2)EU ME GARANTO. \n(3)SOU FERA! MANDA VER!\nESCOLHA O NÍVEL DE DIFICULDADE:"))

    if (dificuldade == 1):
        print("VOCÊ POSSUI 7 TENTATIVAS! VAMOS LÁ!")
        break
    elif (dificuldade == 2):
        print ("VOCÊ POSSUI 5 TENTATIVAS! VAMOS LÁ!")
        break
    elif (dificuldade == 3):
        print ("VOCÊ POSSUI 3 TENTATIVAS! VAMOS LÁ!")
        break
    else:
        print("ESTA NÃO É UMA OPÇÃO, DIGITE UM NÚMERO VÁLIDO:")
        continue

for tentativa in range (1, total_de_tentativas = 1):
    print("VOCÊ USOU" ,tentativa, "DE" ,total_de_tentativas)

    valor_usuario = int(input("SERÁ QUE VOCÊ ACERTA? DIGITE UM NÚMERO DE 1 A 100."))

    if (valor_usuario < 1 or valor_usuario > 100):
        print("NÚMERO INVÁLIDO. TENTE OUTRA VEZ!")

    valor_correto = valor_usuario == numero_sorteado
    valor_maior = valor_usuario > numero_sorteado
    valor_menor = valor_usuario < numero_sorteado

    if (valor_correto):
        print("PARABÉNS! VOCÊ CONSEGUIU ACERTAR O NÚMERO ESCOLHIDO POR MIM!")
        break

    else:
        if (valor_maior):
            print("O NÚMERO ESCOLHIDO POR MIM É MENOR QUE O NÚMERO SUGERIDO POR VOCÊ.")

        if (valor_menor):
            print("O NÚMERO ESCOLHIDO POR MIM É MAIOR QUE O NÚMERO SUGERIDO POR VOCÊ.")

print("FIM DE JOGO!")
