import time
import random

# define the board of tic tac toe
board = {
    '0': 0, '1': 1, '2': 2,
    '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8
}


def show_board():  # show the board of tic tac toe
    print(str(board['0']) + ' | ' + str(board['1']) + ' | ' + str(board['2']))
    print('--|---|--')
    print(str(board['3']) + ' | ' + str(board['4']) + ' | ' + str(board['5']))
    print('--|---|--')
    print(str(board['6']) + ' | ' + str(board['7']) + ' | ' + str(board['8']))


def first_move_bot():  # choose who will move first? bot or player?
    global turn
    print('Choosing who will take the first turn, Patience is necessary')
    time.sleep(1.5)
    choose = random.randint(1, 2)
    if choose == 1:
        print('Bot will move first !')
        turn = 'O'
    else:
        print('Player will move first !')
        turn = 'X'


def check_board_bot():
    global turn
    global winning
    winning = False
    win = {'O': 'Bot', 'X': 'Player'}
    if board['0'] == board['1'] == board['2'] or board['3'] == board['4'] == board['5'] or board['6'] == board['7'] == board['8']:
        print(win[turn] + ' won the match!')
        winning = True
    elif board['0'] == board['3'] == board['6'] or board['1'] == board['4'] == board['7'] or board['2'] == board['5'] == board['8']:
        print(win[turn] + ' won the match!')
        winning = True
    elif board['0'] == board['4'] == board['8'] or board['2'] == board['4'] == board['6']:
        print(win[turn] + ' won the match!')
        winning = True


round = input('Enter the game\'s round(s) : ')
making_sure = input('Do you want to play the game with ' +
                    round + ' round(s)? (yes/no) ')

while making_sure != 'yes':
    round = input('Enter the game\'s round(s) : ')
    making_sure = input('Do you want to play the game with ' +
                        round + ' round(s)? (yes/no) ')


print('Choose game mode :\n1. VS Player\n2. VS Bot')
answer = input('Answer (in number) : ')

while answer != '1' and answer != '2':
    print('Your answer is not recognized! Please try again!')
    print('Choose game mode :\n1. VS Player\n2. VS Bot')
    time.sleep(1.5)
    answer = input('Answer (in number) : ')

options_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

win = 0
lose = 0
draw = 0

def round_stats_counter_bot():
    global win, lose, draw
    if winning == True:
        if turn == 'O':
            lose += 1
        elif turn == 'X':
            win += 1
        print('Player : ' + str(win) + ' win(s) ' + str(lose) + ' lose(s) ' + str(draw) + ' draw(s)')
    elif winning == False and game == 9:
        draw += 1
        print('Player : ' + str(win) + ' win(s) ' + str(lose) + ' lose(s) ' + str(draw) + ' draw(s)')

if answer == '2':

    first_move_bot()

    show_board()

    # process
    for rounds in range(int(round)):
        for game in range(1, 10):
            time.sleep(1.5)
            if turn == 'O':
                print('Bot\'s turn')
                time.sleep(1.5)
                bot = int(random.randint(0, 8))

                while bot not in options_list:
                    bot = random.randint(0, 8)

                board[str(bot)] = turn
                options_list.remove(bot)
            else:
                print('Player\'s turn')
                time.sleep(1.5)

                for options in options_list:
                    print(options)

                player = input('Enter your choice based on the options above : ')

                while int(player) not in options_list:
                    print('Your choice is not recognized! Please re-enter your choice!')
                    for options in options_list:
                        print(options)
                    player = input(
                        'Enter your choice based on the options above : ')

                board[player] = turn
                options_list.remove(int(player))

            show_board()
            check_board_bot()

            round_stats_counter_bot()

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

            if winning == True:
                if (rounds + 1) != int(round):
                    print('Round ' + str(rounds + 2) + ' starts!')
                    options_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                    x = 0
                    
                    for check in range(len(board.keys())):
                        if board[str(x)] != x:
                            board.update({str(x):x})
                        x += 1
                    
                time.sleep(1.5)
                break

elif answer == '1':

    player1 = input('Enter player 1\'s name : ')
    player2 = input('Enter player 2\'s name : ')

    time.sleep(1.5)

    def first_move_player():  # choose who will move first? bot or player?
        global turn
        print('Choosing who will take the first turn, Patience is necessary')
        time.sleep(1.5)
        choose = random.randint(1, 2)
        if choose == 1:
            print(player1 + ' will move first !')
            turn = 'O'
        else:
            print(player2 + ' will move first !')
            turn = 'X'

    def check_board_player():
        global turn
        global winning
        winning = False
        win = {'O': 'Player 1', 'X': 'Player 2'}
        if board['0'] == board['1'] == board['2'] or board['3'] == board['4'] == board['5'] or board['6'] == board['7'] == board['8']:
            print(win[turn] + ' won the match!')
            winning = True
        elif board['0'] == board['3'] == board['6'] or board['1'] == board['4'] == board['7'] or board['2'] == board['5'] == board['8']:
            print(win[turn] + ' won the match!')
            winning = True
        elif board['0'] == board['4'] == board['8'] or board['2'] == board['4'] == board['6']:
            print(win[turn] + ' won the match!')
            winning = True

    first_move_player()

    time.sleep(1.5)

    show_board()

    player1_win = 0
    player1_lose = 0
    player2_win = 0
    player2_lose = 0
    draw = 0

    def round_stats_counter_player():
        global player1_lose, player1_win, player2_lose, player2_win, draw
        if winning == True:
            if turn == 'O':
                player1_win += 1
                player2_lose += 1
            else:
                player1_lose += 1
                player2_win += 1
            print('Player 1 : ' + str(player1_win) + ' win(s) ' + str(player1_lose) + ' lose(s) ' + str(draw) + ' draw(s)')
            print('Player 2 : ' + str(player2_win) + ' win(s) ' + str(player2_lose) + ' lose(s) ' + str(draw) + ' draw(s)')
        elif winning == False and game == 9:
            draw += 1
            print('Player 1 : ' + str(player1_win) + ' win(s) ' + str(player1_lose) + ' lose(s) ' + str(draw) + ' draw(s)')
            print('Player 2 : ' + str(player2_win) + ' win(s) ' + str(player2_lose) + ' lose(s) ' + str(draw) + ' draw(s)')
        

    for rounds in range(int(round)):
        for game in range(1, 10):
            time.sleep(1.5)
            if turn == 'O':
                print(player1 + '\'s turn')
                time.sleep(1.5)

                for options in options_list:
                    print(options)

                player = input('Enter your choice based on the options above : ')

                while int(player) not in options_list:
                    print('Your choice is not recognized! Please re-enter your choice!')
                    for options in options_list:
                        print(options)
                    player = input(
                        'Enter your choice based on the options above : ')

                board[player] = turn
                options_list.remove(int(player))
            else:
                print(player2 + '\'s turn')
                time.sleep(1.5)

                for options in options_list:
                    print(options)

                player = input('Enter your choice based on the options above : ')

                while int(player) not in options_list:
                    print('Your choice is not recognized! Please re-enter your choice!')
                    for options in options_list:
                        print(options)
                    player = input(
                        'Enter your choice based on the options above : ')

                board[player] = turn
                options_list.remove(int(player))

            show_board()
            check_board_player()

            round_stats_counter_player()

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

            if winning == True:
                if (rounds + 1) != int(round):
                    print('Round ' + str(rounds + 2) + ' starts!')
                    options_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                    x = 0
                    
                    for check in range(len(board.keys())):
                        if board[str(x)] != x:
                            board.update({str(x):x})
                        x += 1
                    
                time.sleep(1.5)
                break

            
