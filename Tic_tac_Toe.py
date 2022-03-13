# Global Variable
player1 = True
player2 = False
count = 0
winner = None
again = True
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# Display Board
def display_board():
    print(board[0], '|', board[1], '|', board[2])
    print("--*---*--")
    print(board[3], '|', board[4], '|', board[5])
    print("--*---*--")
    print(board[6], '|', board[7], '|', board[8])


# Function for randomlly changing player
def changing_player():

    global player1
    global player2

    from random import randint
    change = randint(1, 2)

    if change == 1:
        player1 = True
        player2 = False
    elif change == 2:
        player1 = False
        player2 = True


# Function for checking result
def check_result():
    global winner

    # check_rows
    if board[0] == board[1] == board[2] != ' ':
        winner = board[0]
    elif board[3] == board[4] == board[5] != ' ':
        winner = board[3]
    elif board[6] == board[7] == board[8] != ' ':
        winner = board[6]

    # check_column
    if board[0] == board[3] == board[6] != ' ':
        winner = board[0]
    elif board[1] == board[4] == board[7] != ' ':
        winner = board[1]
    elif board[2] == board[5] == board[8] != ' ':
        winner = board[2]

    # check_diagonal
    if board[0] == board[4] == board[8] != ' ':
        winner = board[0]
    elif board[6] == board[4] == board[2] != ' ':
        winner = board[6]

# Taking input from player


def user_input():
    global player1
    global player2
    global count
    global winner

    # Random player chose
    changing_player()

    while count != 9:
        while player1:
            position = input("Enter the number between 1 to 9 for X: ")
            while position not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                position = input("Invalid Input. Please try again")
            position = int(position) - 1
            if board[position] == ' ':
                board[position] = 'X'
                count += 1
                display_board()
                player1 = False
                player2 = True
                check_result()
                if winner == 'X' or winner == 'O':                 # Winner check
                    print(f'{winner} is winner')
                    count = 9
                    player2 = False
                    break
                if count == 9:                                     # Tie Condition
                    player2 = False
                    print("Game is Tie")
                    break
            else:
                print("space is not empty. Try another position")

        while player2:
            position = input("Enter the number between 1 to 9 for O: ")
            while position not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                position = input("Invalid Input. Please try again")
            position = int(position) - 1
            if board[position] == ' ':
                board[position] = 'O'
                count += 1
                display_board()
                player2 = False
                player1 = True
                check_result()
                if winner == 'X' or winner == 'O':                 # Winner check
                    print(f'{winner} is winner')
                    count = 9
                    player1 = False
                    break
                if count == 9:                                    # Check Condition
                    player1 = False
                    print("Game is Tie")
                    break
            else:
                print("space is not empty. Try another position")


# Main Function
def main_game():
    global player1
    global player2
    global count
    global winner
    global again
    global board

    while again == True:
        display_board()
        user_input()
        ans = input("Press Y to play again ")

        # Reseting the board and winner
        if ans.capitalize() == "Y":
            player1 = True
            player2 = False
            count = 0
            winner = None
            board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        else:
            again = False
            print("Game over!")

main_game()
