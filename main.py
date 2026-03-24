#GS & M7
from random import randint

#Listas usadas por cada oponente para decidir a jogada
oponents = [['pedra', 'papel', 'tesoura'], 
            ['pedra', 'pedra', 'pedra', 'pedra', 'pedra', 'pedra', 'pedra', 'pedra', 'papel', 'tesoura'], 
            ['tesoura', 'tesoura'], 
            ['papel']]

valid_moves = ['pedra', 'papel', 'tesoura']

#Função que escolhe oponete
def choose():
            while True:
                        choice = input('Escolha o modo de jogo que deseja jogar digitando o número correspondente e apertando ENTER. \n' \
                                    '0 - Aleatorionildo\n' \
                                    '1 - Pedro Pedra\n' \
                                    '2 - Edward\n' \
                                    '3 - Papeleiro Maluco\n')
                        
                        #Filtro de respostas possíveis (Repete até que cumpra ambas as exigências)
                        if choice.isnumeric() == True:
                                    choice = int(choice)
                                    if choice < len(oponents):
                                                return int(choice)
                                    print("\nNúmero inválido, escolha dentre as opções apresentadas. \n\n")
                                    continue
                        print("\nPor favor escreva somente o número do oponente que deseja enfrentar. \n\n")

#Função do jogo em si (usa a resposta da seleção para determinar qual das listas usar)
def game_start(oponent):
            #Seleciona a lsita correta para o inimigo
            pool = oponents[int(oponent)]
            print('\nEntão vamos começar o jogo. \n\n')

            #Define as variáveis de contagem de pontos
            playerspoints = 0
            enemyspoints = 0

            #Define que o jogo se repita até que algum dos lados consiga 2 pontos (vitória em melhor de 3)
            while playerspoints < 2 and enemyspoints < 2:
                        #Garante que jogada do jogador seja válida (continue prossegue o loop sem executar nenhum comando, 
                        #Ou seja pode repetir quantas vezes for preciso)
                        playersplay = str(input('Escolha entre pedra, papel e tesoura para jogar. ')).lower()
                        if playersplay not in valid_moves:
                                    print("\nEscolha uma jogada válida (pedra, papel ou tesoura). \n\n")
                                    continue
                        #Escolhe aleatoriamente um elemento da lista do oponente
                        rand = randint(0, len(pool)-1)
                        enemysplay = pool[rand]

                        #Caso 1: Player ganha
                        if playersplay == 'tesoura' and enemysplay == 'papel' or \
                                    playersplay == 'pedra' and enemysplay == 'tesoura' or \
                                    playersplay == 'papel' and enemysplay == 'pedra':
                                    playerspoints += 1
                                    print('Você ganhou uma. O placar está: \nVocê: {}\nOponente: {}'.format(playerspoints, enemyspoints))

                        #Caso 2: Empate
                        elif playersplay == enemysplay:
                                    print('Empate! Ninguém ganha nada. ')

                        #Caso 3: Oponente ganha (já que os casos de entrada inválida foram filtrados acima é possível usar o else)
                        else: 
                                    enemyspoints += 1
                                    print('Você perdeu uma. O placar está: \nVocê: {}\nOponente: {}\n\n'.format(playerspoints, enemyspoints))

            if playerspoints == 2:
                        print('Você ganhou a melhor de três. Parabéns!!!')
                
            elif enemyspoints == 2:
                        print('Você perdeu a melhor de três. WOMP WOMP.')
                        
            print('\nO placar final ficou: \nVocê: {}\nOponente: {}'.format(playerspoints, enemyspoints))

game_start(choose())
