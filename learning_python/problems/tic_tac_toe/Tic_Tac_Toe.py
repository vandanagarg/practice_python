# test_board = ['0','1','2','3','4','5','6','7','8','9']
            # test_board = ['#','X','O','X','O','X','O','X','O','X']
def display_board(test_board):
    # print("\n" * 100)
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

# display_board(test_board)


def player_input():
    marker = ' '
    # Keep asking player 1 to choose X or O
    while marker != 'X' and marker != "O":
        marker = input("Player 1, choose X or O: ").upper()

        # Assign player 2. the opposite marker
    player1_marker = marker

    if player1_marker == 'X':
        player2_marker = "O"
    else:
        player2_marker = "X"

    return (player1_marker, player2_marker)

# player1_marker, player2_marker = player_input()


def place_marker(test_board, marker, position):
    test_board[position] = marker
    display_board(test_board)

# def place_marker( ):
#     # position = int(input(" Please enter your number: "))
#     # test_board[position] =  marker
#
#     n = 0
#     while n < 9:
#     # position = print(input("Please enter a number: "))
#     # n += 1
#     # # print(n)
#
#         if n%2 == 0:
#             position = int(input("Player 1: Please enter your number: "))
#             #print(position)
#             #index_value = int(position)
#             #print(position)
#             test_board[position] = player1_marker
#             display_board(test_board)
#
#         else:
#             position =  int(input("Player 2: Please enter your number: "))
#             #print(position)
#             #index_value = int(position)
#             #print(position)
#             test_board[position] = player2_marker
#             display_board(test_board)
#
#     n += 1


import random

def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return "Player1"
    else:
        return "Player2"

# print(choose_first())

def space_check(test_board, position ):

    return test_board[position] == ' '

#space_check()

def full_board_check(test_board):
    for i in range(1,10):
        if space_check(test_board,i):
            return False
        # board is full if we return true
        #else:
    return True

# full_board_check(test_board)

def player_choice(test_board):

    position = 0

    while position not in range(1,10) or not space_check(test_board, position):
        position = int(input("Choose a position : (1-9) "))

        return position

# player_choice(test_board)


def replay():

    choice = input("Play again? Enter Yes or No ")
    return choice == 'Yes'

# replay()


def win_check(test_board, marker):

    #Win tic tac toe?
    # check all rows, columns  and diagonals

    return ((test_board[7] == test_board[8] == test_board[9] == marker) or
            (test_board[4] == test_board[5] == test_board[6] == marker) or
            (test_board[1] == test_board[2] == test_board[3] == marker) or
            (test_board[7] == test_board[4] == test_board[1] == marker) or
            (test_board[8] == test_board[5] == test_board[2] == marker) or
            (test_board[9] == test_board[6] == test_board[3] == marker) or
            (test_board[7] == test_board[5] == test_board[3] == marker) or
            (test_board[9] == test_board[5] == test_board[1] == marker))



#WHILE LOOP TO KEEP RUNNING THE GAME

print("Welcome to Tic Tac Toe")

while True:
    #Play the Game


    ## Set everything (Board, who's first, choose markers X, O)
    #test_board = ['0','1','2','3','4','5','6','7','8','9']
    test_board = [' '] * 10

    turn = choose_first()
    print(turn + " will go first.")

    player1_marker, player2_marker = player_input()
    #print(player_input())

    play_game = input(("Ready to play? Yes or No? "))

    if play_game == "Yes":
        game_on = True
    else:
        game_on = False

    ##Game Play

    while game_on:

        if turn == "Player1":

            #Show the board
            #print(display_board(test_board))
            display_board(test_board)

            #choose a position
            position = player_choice(test_board)

            #Place the marker on the position
            #print(place_marker(test_board, player1_marker, position))
            place_marker(test_board, player1_marker, position)

            #Check if they won
            # Check if there is as a tie
            # No tie and no win? The next player's turn.
            ###Player one turn
            if win_check(test_board, player1_marker):
                display_board(test_board)
                print("Player 1 has won!! ")

                game_on = False

            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print("Tie Game!")

                    game_on = False

                else:
                    turn = "Player2"


        else:
            ###Player two turn
            # Show the board
            #print(display_board(test_board))
            display_board(test_board)

            # choose a position
            position = player_choice(test_board)

            # Place the marker on the position
            #print(place_marker(test_board, player2_marker, position))
            place_marker(test_board, player2_marker, position)

            # Check if they won
            # Check if there is as a tie
            # No tie and no win? The next player's turn.
            ###Player one turn
            if win_check(test_board, player2_marker):
                display_board(test_board)
                print("Player 2 has won!! ")

                game_on = False

            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print("Tie Game!")

                    game_on = False

                else:
                    turn = "Player1"

if True:
    vandana

if not replay():
    break
    #Break out of the while loop on replay()