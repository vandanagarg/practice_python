def display_board(test_board):
    print(test_board[7] + "|" + test_board[8] + "|" + test_board[9])
    print("_|_|_")
    print(test_board[4] + "|" + test_board[5] + "|" + test_board[6])
    print("_|_|_")
    print(test_board[1] + "|" + test_board[2] + "|" + test_board[3])
    print(" | | ")


def choose_sign():
    input_symbol = input("Player1: Please choose your symbol X or O")
    player_1_symbol = input_symbol.upper()
    if input_symbol.upper() == "X":
        player_2_symbol = "O"
    else:
        player_2_symbol = "X"
    print("Player 1 symbol is : " + player_1_symbol)
    print("Player 2 symbol is : " + player_2_symbol)
    return player_1_symbol, player_2_symbol


def place_marker(test_board, marker, position):
    test_board[position] = marker
    display_board(test_board)

def check_space(test_board):
    for place in test_board:
        return test_board[place] == " "

def won_game(test_board, marker):
    return (
        (test_board[7] == test_board[8] == test_board[9] == marker)
        or (test_board[4] == test_board[5] == test_board[6] == marker)
        or (test_board[1] == test_board[2] == test_board[3] == marker)
        or (test_board[7] == test_board[4] == test_board[1] == marker)
        or (test_board[5] == test_board[8] == test_board[2] == marker)
        or (test_board[6] == test_board[3] == test_board[9] == marker)
        or (test_board[7] == test_board[5] == test_board[3] == marker)
        or (test_board[9] == test_board[5] == test_board[1] == marker)
    )

def check_tie(test_board):
    if (not check_space()) and (not won_game()):
        print("It's a tie!")
        print("You may try another game.")
    else:
        exit()


def replay():
    play_again = input("Do you want to play again ? Yes or No")
    if play_again == "Yes":
        choose_sign()


#main program
def play_game():

    test_board = [" "," "," "," "," "," "," "," "," "," "]
    display_board(test_board)
    player1_symbol, player2_symbol = choose_sign()

    n =1
    while n< 10:
        position = int(input("Choose number 1-9"))

        if n%2 != 0:
            place_marker(test_board, player1_symbol,position)
            if won_game(test_board,player1_symbol):
                print("Player1 has won the game.")
                break

        elif n%2 == 0:
            place_marker(test_board, player2_symbol, position)
            if won_game(test_board,player2_symbol):
                print("Player2 has won the game.")
                break

        n += 1

    if n == 10:
        print("No one has won, it's a tie. Play again :) ")

    play_again = input("Do you want to play again? Yes or No")
    if play_again == "Yes":
        play_game()



play_game()