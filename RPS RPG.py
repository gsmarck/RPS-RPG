from random import randint

oponents = [['pedra', 'papel', 'tesoura'], 
            ['pedra', 'pedra', 'pedra', 'pedra', 'pedra', 'pedra', 'pedra', 'pedra', 'papel', 'tesoura'], 
            ['pedra', 'papel', 'tesoura', 'tesoura', 'tesoura', 'tesoura'], 
            ['papel']]

valid_moves = ['pedra', 'papel', 'tesoura']

def choose():
    while True:
        choice = input('Escolha o modo de jogo que deseja jogar digitando o número correspondente e apertando ENTER. \n' \
                '0 - Aleatorionildo\n' \
                '1 - Pedro Pedra\n' \
                '2 - Edward\n' \
                '3 - Papeleiro Maluco\n')
        if choice.isnumeric() == True:
            choice = int(choice)
            if choice < len(oponents):
                return int(choice)

def game_start(oponent):
    pool = oponents[int(oponent)]
    print('\nEntão vamos começar o jogo. \n\n')

    playerspoints = 0
    enemyspoints = 0
    while playerspoints < 2 and enemyspoints < 2:
        playersplay = str(input('Escolha entre pedra, papel e tesoura para jogar. ')).lower()
        if playersplay not in valid_moves:
            continue
        rand = randint(0, len(pool)-1)
        enemysplay = pool[rand]
        if playersplay == 'tesoura' and enemysplay == 'papel' or playersplay == 'pedra' and enemysplay == 'tesoura' or playersplay == 'papel' and enemysplay == 'pedra':
            playerspoints += 1
            print('Você ganhou uma. O placar está: \nVocê: {}\nOponente: {}'.format(playerspoints, enemyspoints))
        elif playersplay == enemysplay:
            print('Empate! Ninguém ganha nada. ')
        else: 
            enemyspoints += 1
            print('Você perdeu uma. O placar está: \nVocê: {}\nOponente: {}\n\n'.format(playerspoints, enemyspoints))

    if playerspoints == 2:
        print('Você ganhou a melhor de três. Parabéns!!!')
    elif enemyspoints == 2:
        print('Você perdeu a melhor de três. WOMP WOMP.')
    print('\nO placar final ficou: \nVocê: {}\nOponente: {}'.format(playerspoints, enemyspoints))

game_start(choose())
