from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9])
    print('--------')
    print(' '+board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6]) 
    print('--------')
    print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3])


def player_input():    
    marker = ''    
    # KEEP ASKING PLAYER 1 TO CHOSE X OR O    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, chose X or O: ')
    player1 = marker
    # ASSIGN PLAYER 2 THE OPPOSITE MARKER
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)


def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ''


def full_board_check(board):
    return all(board) != None


def place_marker(board, marker, position):
    board[position] = marker

    
def player_choice(board):
    position = ''
    while position == '':
        position = int(input('What is your next positon? '))
        if position >= 1 and position <= 9: # FIX THIS - PUTTING IN A LETTER BREAKS GAME
            if space_check(board,position) == True:
                return position
            else:
                print('That position is used. Try again')
                position = ''
        else:
            print('That number is not 1-9.')
            position = ''


def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    

def replay():
    play_again = str(input('Do you want to play again? Y or N.'))
    return play_again.lower()[0] == 'y'


print('Welcome to Tic Tac Toe!')


while True:
    # Set the game up here
    theBoard = ['']*10
    display_board(theBoard)
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    play_game = input('Are you ready to play? Enter Yes or No. ')
    if play_game.lower()[0] ==  'y':
        print('Yes')
        game_on = True
    else:
        game_on = False

    while game_on:

        #Player 1 Turn
        if turn == 'Player 1':
            display_board(theBoard)
            print("Player 1 Turn")
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            if win_check(theBoard,player1_marker) == True:
                display_board(theBoard)                
                print('You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard) == False:
                    
                    print('Full board!')
                    game_on = False
                else:
                    turn = 'Player 2'
            pass
        # Player2's turn.
        else:    
            display_board(theBoard)
            print("Player 2 Turn")
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)
            if win_check(theBoard,player2_marker) == True:
                
                display_board(theBoard)
                print('You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard) == False:
                    print('Full board! Draw!')
                    game_on = False
                else: 
                    turn = 'Player 1'
            pass
        
    if not replay():
        break