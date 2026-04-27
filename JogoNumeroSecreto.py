from random import randint

while True:
    #Número Aleatório
    ns = randint(0, 100)
    #Variáveis
    numrod = 2
    i = 1
    pont = 1100
    print('Vou pensar em um número, tente adivinhar!')
    print(ns)
    #Selecione a Dificuldade.
    print('Dificuldades: \n(1) Fácil\n(2) Médio\n(3) Difícil')
    dif = int(input('Selecione a dificuldade: '))

    #Estrutura While dificuldade
    if dif == 1:
        numrod=11
    elif dif == 2:
        numrod=8
        pont = 1600
    elif dif == 3:
        numrod=6
        pont = 6000
    else:
        pont = 2000000
        print('Dificuldade secreta desbloqueada! NÍVEL IMPOSSÍVEL!')
    while i <= numrod:
        tent= int(input(f'Tentativa {i} de {numrod-1}, digite um número: '))
        i += 1
        while i <= numrod:
            if dif == 2:
                pont-=200
            elif dif == 3:
                pont-=1000
            elif dif != 1 and 2 and 3:
                pont-=1000000
            else:
                pont -= 100
            break
        if tent == ns:
            print('PARABÉNS!!! VOCÊ ACERTOU!')
            break
        elif i == numrod:
            print('Suas chances acabaram :(')
            break
        #Dicas
        elif ns<tent:
            print('O número secreto é menor.')
        elif ns>tent:
            print('O número secreto é maior.')
    print(f'Você fez {pont} pontos!')
    print('FIM DE JOGO.')

#Jogar Denovo?

    resp=input('Você deseja jogar? ("S" para Sim e "N" para Não): ').lower()
    if resp == 'n':
        print('Tchau, até mais!')
        break