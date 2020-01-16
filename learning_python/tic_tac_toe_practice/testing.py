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
    player1 = marker

    if player1 == 'X':
        player2 = "O"
    else:
        player2 = "X"

    return (player1, player2)

# player1_marker, player2_marker = player_input()




# def place_marker(test_board, marker, position):
#     display_board[position] = marker
#
# print(place_marker())

# n = 0
# while n < 9:
#     # position = print(input("Please enter a number: "))
#     # n += 1
#     # # print(n)
#
#     if n%2 == 0:
#         position = int(input("Player 1: Please enter your number: "))
#         #print(position)
#         #index_value = int(position)
#         #print(position)
#         test_board[position] = player1_marker
#         display_board(test_board)
#
#     else:
#         position =  int(input("Player 2: Please enter your number: "))
#         #print(position)
#         #index_value = int(position)
#         #print(position)
#         test_board[position] = player2_marker
#         display_board(test_board)
#
#     n += 1
#


def place_marker( ):
    # position = int(input(" Please enter your number: "))
    # test_board[position] =  marker

    n = 0
    while n < 9:
    # position = print(input("Please enter a number: "))
    # n += 1
    # # print(n)

        if n%2 == 0:
            position = int(input("Player 1: Please enter your number: "))
            #print(position)
            #index_value = int(position)
            #print(position)
            test_board[position] = player1_marker
            display_board(test_board)

        else:
            position =  int(input("Player 2: Please enter your number: "))
            #print(position)
            #index_value = int(position)
            #print(position)
            test_board[position] = player2_marker
            display_board(test_board)

    n += 1


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
        #board is full if we return true
        return True

# full_board_check(test_board)

def player_choice(test_board):

    position = 0

    while position not in range(1,10) or not space_check(test_board, position):
        position = int(input("Choose a position : (1-9) "))

        return position

# player_choice(test_board)


def replay():

    choice = input("Play again? Enter Yes or No")
    return choice == 'Yes'

# replay()


def win_check(test_board, mark):

    #Win tic tac toe?
    # check all rows, columns  and diagonals

    return ((test_board[7] == test_board[8] == test_board[9] == mark) or
            (test_board[4] == test_board[5] == test_board[6] == mark) or
            (test_board[1] == test_board[2] == test_board[3] == mark) or
            (test_board[7] == test_board[4] == test_board[1] == mark) or
            (test_board[8] == test_board[5] == test_board[2] == mark) or
            (test_board[9] == test_board[6] == test_board[3] == mark) or
            (test_board[7] == test_board[5] == test_board[3] == mark) or
            (test_board[9] == test_board[5] == test_board[1] == mark))



#WHILE LOOP TO KEEP RUNNING THE GAME

print("Welcome to Tic Tac Toe")

while True:
    #Play the Game


    ## Set everything (Board, who's first, choose markers X, O)
    test_board = ['0','1','2','3','4','5','6','7','8','9']

    player1_marker, player2_marker = player_input()
    #print(player_input())

    turn = choose_first()
    print(turn + "will go first.")

    play_game = input(("Ready to play? Yes or No? "))

    if play_game =="Yes":
        game_on = True
    else:
        game_on = False

    ##Game Play

    while game_on:

        if turn == "Player 1":

            #Show the board
            print(display_board(test_board))

            #choose a position
            position = player_choice(test_board)

            #Place the marker on the position
            print(place_marker())
            #place_marker(test_board, player1_marker, position)

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
                    turn = "Player 2"


        else:
            ###Player two turn
            # Show the board
            print(display_board(test_board))

            # choose a position
            position = player_choice(test_board)

            # Place the marker on the position
            print(place_marker())
            # place_marker(test_board, player1_marker, position)

            # Check if they won
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
                    turn = "Player 1"




    if not replay():
        break
        #Break out of the while loop on replay()


#tic tac toe board

def tic_tac_toe():

    def start_game():
        status = input(" Are you ready to begin the game 'Yes' or 'No'.")
        if status == "Yes":
            player1 = input("Please pick a marker 'X' or 'O'.")
            # print("\n" * 100)

            test_board = [" "] * 10
            # test_board = ['#','X','O','X','O','X','O','X','O','X']
            #display_board(test_board)

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

                def player_input():

                    marker = ' '
                    #Keep asking player 1 to choose X or O
                    while marker != 'X' and marker != "O":
                        marker = input("Player 1, choose X or O: ").upper()

                        #Assign player 2. the opposite marker
                    player1 = marker

                    if player1 == 'X':
                        player2 = "O"
                    else:
                        player2 = "X"

                    return (player1,player2)

                player1_marker , player2_marker = player_input()

                position = int(input("Please enter a number: ")
                def place_marker(test_board, marker, position):
                    display_board[position] = marker


                def check_win():
                    if test_board[7] == test_board[8] ==test_board[9] == player1_marker or test_board[7] == test_board[8] ==test_board[9] == player2_marker or
                       test_board[4] == test_board[5] == test_board[6] == player1_marker or test_board[4] == test_board[5] == test_board[6] == player2_marker or
                       test_board[1] == test_board[2] == test_board[3] == player1_marker or test_board[1] == test_board[2] == test_board[3] == player2_marker or
                       test_board[7] == test_board[4] == test_board[1] == player1_marker or test_board[7] == test_board[4] == test_board[1] == player2_marker or
                       test_board[8] == test_board[5] == test_board[2] == player1_marker or test_board[8] == test_board[5] == test_board[2] == player2_marker or
                       test_board[9] == test_board[6] == test_board[3] == player1_marker or test_board[9] == test_board[6] == test_board[3] == player2_marker or
                       test_board[7] == test_board[5] == test_board[3] == player1_marker or test_board[7] == test_board[5] == test_board[3] == player2_marker or
                       test_board[9] == test_board[5] == test_board[1] == player1_marker or test_board[9] == test_board[5] == test_board[1] == player2_marker :


                def check_tie():

                    def slice_from_element(inp_array, num):
                        output_array = []
                        for index in range(0, len(inp_array)):
                            # print(inp_array[index])
                            if inp_array[index] != num:
                                continue
                            else:
                                index_val = index + 1
                                for new_index in range(index_val, len(inp_array)):
                                    output_array.append(inp_array[new_index])
                                return output_array
                                # return  inp_array[index_val:]

                    print(slice_from_element(inp_array, num))



        #
        # else:
        #     break

# from IPython.display import clear_output
# clear_output()


# print(tic_tac_toe())




# list = ['O','X','O','X','O','X','X','X','O']
#
# def who_won(list):
#
#     Player1 = "X"
#     Player2 = "O"
#
#
#
#     # if marker == 'X':
#     #     player = "Player1"
#     # elif marker == "O":
#     #     player = "Player2"
#
# if ((list[0]== list[1]== list[2] == 'X' or 'O') or
#     (list[3] == list[4] == list[5] == 'X' or 'O') or
#     (list[6] == list[7] == list[8] == 'X' or 'O') or
#     (list[6] == list[3] == list[0] == 'X' or 'O') or
#     (list[7] == list[4] == list[1] == 'X' or 'O') or
#     (list[2] == list[5] == list[8] == 'X' or 'O') or
#     (list[6] == list[4] == list[2] == 'X' or 'O') or
#     (list[4] == list[0] == list[8] == 'X' or 'O')):
#     print("You won.")
#
# else:
#     print("Lost.")


# def sum_a_b(a,b):
#     return a+b
#
# print(sum_a_b(2,2))
# print(sum_a_b(5,6))


# list2 = [1,0,1,0,1,1,1]
# #[0,2,4,5,6]
# list3 = []
# index_val = [0,2,4,5,6]
# for val in range(0, len(index_val)):
#     #print(list2[index_val[val]])
#     list3.append(list2[index_val[val]])
# print(list3)


# list = ['O','X','O','X','O','X','X','X','O']
#
# mark = "X" or "O"
# Player1 = "X"
# Player2 = "O"
#
# def who_won(list):
#
#     if ((list[0]== list[1]== list[2] == mark) or
#       (list[3] == list[4] == list[5] == mark) or
#       (list[6] == list[7] == list[8] == mark) or
#       (list[6] == list[3] == list[0] == mark) or
#       (list[7] == list[4] == list[1] == mark) or
#       (list[2] == list[5] == list[8] == mark) or
#       (list[6] == list[4] == list[2] == mark) or
#       (list[4] == list[0] == list[8] == mark)):
#       print("You won.")
#
# else:
#     print("Lost.")


