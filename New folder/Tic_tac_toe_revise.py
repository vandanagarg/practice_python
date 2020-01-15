# class TicTacToe:


# test_board = ['0','1','2','3','4','5','6','7','8','9']

def display_board(test_board):
    print("   |   |   ")
    print(" " + test_board[7] + " | " + test_board[8] + " | " + test_board[9] + " ")
    print("   |   |   ")
    print("___ ___ ___")
    print("   |   |   ")
    print(" " + test_board[4] + " | " + test_board[5] + " | " + test_board[6] + " ")
    print("   |   |   ")
    print("___ ___ ___")
    print("   |   |   ")
    print(" " + test_board[1] + " | " + test_board[2] + " | " + test_board[3] + " ")
    print("   |   |   ")


def player_input():
    player1_input = input("Player1 : Choose your sign X or O")
    print("Player1 symbol is: " + player1_input.upper())
    if player1_input.upper() == "X":
        player2_input = "O"
    else:
        player2_input = "X"
    print("Player2 symbol is: " + player2_input.upper())
    return player1_input.upper(), player2_input.upper()


def who_won(test_board, marker):

    if ((test_board[1] == test_board[2] == test_board[3] == marker) or
        (test_board[4] == test_board[5] == test_board[6] == marker) or
        (test_board[7] == test_board[8] == test_board[9] == marker) or
        (test_board[6] == test_board[3] == test_board[9] == marker) or
        (test_board[7] == test_board[4] == test_board[1] == marker) or
        (test_board[2] == test_board[5] == test_board[8] == marker) or
        (test_board[7] == test_board[5] == test_board[3] == marker) or
        (test_board[5] == test_board[1] == test_board[9] == marker)):
        return True
    else:
        return False

def space_check(test_board, position):
    return test_board[position] == ' '


def is_board_full_check(test_board):
    for i in range(1,10):
        if space_check(test_board,i):
            return False
        #board is full if we return true
    return True


def player_choice(test_board):

    position = 0

    while position not in range(1,10) or not space_check(test_board, position):
        position = int(input("Choose a position : (1-9) "))

        return position


def replay():
    choice = input("Play again? Enter Yes or No")
    return choice == 'Yes'


def place_marker(test_board, marker, position):
    test_board[position] = marker
    display_board(test_board)


import random

def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return "Player1"
    else:
        return "Player2"


#WHILE LOOP TO KEEP RUNNING THE GAME

print("Welcome to Tic Tac Toe")

while True:
    #Play the Game


    ## Set everything (Board, who's first, choose markers X, O)
    # test_board = ['0','1','2','3','4','5','6','7','8','9']
    test_board = [' ', ' ',' ',' ',' ',' ',' ', ' ',' ',' ',' ',' ']

    player1_marker, player2_marker = player_input()
    #print(player_input())

    turn = choose_first()
    print(turn + " will go first.")

    play_game = input(("Ready to play? Yes or No? "))

    if play_game == "Yes":
        game_on = True
    else:
        game_on = False


    ##Game Play

    while game_on:

        if turn == "Player1":

            #Show the board
            display_board(test_board)

            #choose a position
            position = player_choice(test_board)

            #Place the marker on the position
            # print(place_marker())
            place_marker(test_board, player1_marker, position)

            #Check if they won
            # Check if there is as a tie
            # No tie and no win? The next player's turn.
            ###Player one turn
            if who_won(test_board, player1_marker):
                display_board(test_board)
                print("Player 1 has won!! ")

                game_on = False

            else:
                if is_board_full_check(test_board):
                    display_board(test_board)
                    print("Tie Game!")
                    game_on = False

                else:
                    turn = "Player2"


        else:
            ###Player two turn
            # Show the board
            display_board(test_board)

            # choose a position
            position = player_choice(test_board)

            # Place the marker on the position
            # print(place_marker())
            place_marker(test_board, player2_marker, position)

            # Check if they won
            # Check if there is as a tie
            # No tie and no win? The next player's turn.
            ###Player one turn
            if who_won(test_board, player2_marker):
                display_board(test_board)
                print("Player 2 has won!! ")

                game_on = False

            else:
                if is_board_full_check(test_board):
                    display_board(test_board)
                    print("Tie Game!")
                    game_on = False

                else:
                    turn = "Player1"




    if not replay():
        break
        #Break out of the while loop on replay()

