import random
import os

vitoria = 0
jogadas = 0


def limpatela():
    os.system('cls')


while True:

    # lista de animais
    animal = [
        "gato", "cachorro", "elefante", "leao", "tigre",
        "girafa", "macaco", "urso", "lobo", "zebra",
        "cobra", "cavalo", "pato", "peixe", "golfinho",
        "arara", "coruja", "coelho", "camelo", "jacare"
    ]

    frutas = [
        "abacaxi", "banana", "cereja", "damasco", "figo",
        "goiaba", "kiwi", "laranja", "limao", "mamao",
        "manga", "melancia", "melao", "morango",
        "pera", "pessego", "pitanga", "tamarindo", "uva"
    ]

    objetos = [
        "cadeira", "mesa", "garrafa", "caderno", "lapis",
        "caneta", "mochila", "chave", "telefone", "espelho",
        "ventilador", "sofa", "computador", "janela", "porta",
        "armario", "pente", "controle", "colher", "faca"
    ]

    # Palavra aleatória
    while True:
        print("Qual modo deseja jogar?\nAnimal (1)\nFruta  (2)\nObjeto (3)")
        modo = input("Digite o modo desejado: ")

        if modo == '1':
            ps = random.choice(animal)
            dica = 'animal'
            break

        elif modo == '2':
            ps = random.choice(frutas)
            dica = 'fruta'
            break

        elif modo == '3':
            ps = random.choice(objetos)
            dica = 'objeto'
            break

        elif modo not in ['1', '2', '3']:
            print("Não existe essa opção.")

    # lista de chutes
    chute = []
    chance = 5
    i = 0
    letch = ''

    print(f'A palavra sorteada foi: {ps}')

    while i < chance:  # Chances do usuario

        vida = '❤️ ' * (chance - i)

        for letra in ps:
            if letra in chute:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print(' ')

        print(f'A dica é {dica}.')

        letch = input(f'Suas vidas:\n{vida}\nDigite uma letra ou tente a palavra: ').lower()

        chute.append(letch)  # Adicionar na lista de letras chutadas

        limpatela()

        if letch == ps:
            print(f'Você Ganhou! A palavra era {ps}!')
            vitoria += 1
            break

        if letch not in ps:
            i += 1  # Somador de tentativa

        ganhou = True  # O usuario está ganhando, até o programa verificar

        for letra in ps:  # Verificando se o usuario ganhou
            if letra not in chute:  # Se o usuario não preencheu todas as letras necessárias, ele ainda não ganhou
                ganhou = False

        if ganhou == True:  # Verificando se ele ganhou
            print(f'Você Ganhou! A palavra era {ps}!')
            vitoria += 1
            break

        if i == chance:  # Esgotaram as chances do usuário
            print(f'Suas chances acabaram! A palavra era {ps}!')
            break

    jogadas += 1

    r = input('Você deseja jogar novamente? (s/n): ').lower()  # Jogar novamente?

    if r == 'n':
        print('Obrigado por jogar!')
        derrotas = jogadas - vitoria

        print(f"{'-'*5}ESTATÍSTICAS{'-'*5}")
        print(f'Vitórias: {vitoria}')
        print(f'Vezes jogadas: {jogadas}')
        print(f'Derrotas: {derrotas}')

        break