import sys

max_wins = 0
board = {}
turn = 'X'
x_won = 0
o_won = 0
ties = 0

print("----------------------")
print("Let's play Py-Pac-Poe!")
print("----------------------")

def start_game():
    global board, turn, max_wins

    if max_wins == 0:
        try:
            user_input = int(input("Until how many wins do you want to play? "))
            max_wins = user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            start_game()
    board = {
        'a1': " ", 'b1': " ", 'c1': " ",
        'a2': " ", 'b2': " ", 'c2': " ",
        'a3': " ", 'b3': " ", 'c3': " ",
    }
    draw_board()

def draw_board():
    print(f"    A   B   C          SCORE      UNTIL WINS: {max_wins}")
    print()
    print(f"1)  {board['a1']} | {board['b1']} | {board['c1']}          X: {x_won}")
    print("    ----------")
    print(f"2)  {board['a2']} | {board['b2']} | {board['c2']}          O: {o_won}")
    print("    ----------")
    print(f"3)  {board['a3']} | {board['b3']} | {board['c3']}          Ties: {ties}")
    check_winner()
    user_turn()

def user_turn():
    global board, turn
    if turn == "X":
        user_input = input("X turn: ").lower()
        if user_input in ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3',]:
            print("    ----------")
            update_board(user_input) 
        elif user_input == "exit":
            sys.exit(0)
        else:
            draw_board()
    elif turn == "O":
        user_input = input("O turn: ").lower()
        if user_input in ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3',]:
            print("    ----------")
            update_board(user_input) 
        elif user_input == "exit":
            sys.exit(0)
        else:
            print("Illegal move")
            draw_board()

def update_board(str_turn):
    global board, turn
    if board[str_turn] == " ":
        board[str_turn] = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        draw_board()
    elif board[str_turn] != " ":
        print('Illegal move')
        draw_board()

def check_winner():
    empty_cells = any(value == ' ' for value in board.values())
    if (
        (board['a1'] == board['b1'] == board['c1'] != ' ') or
        (board['a2'] == board['b2'] == board['c2'] != ' ') or
        (board['a3'] == board['b3'] == board['c3'] != ' ') or
        
        (board['a1'] == board['a2'] == board['a3'] != ' ') or
        (board['b1'] == board['b2'] == board['b3'] != ' ') or
        (board['c1'] == board['c2'] == board['c3'] != ' ') or
        
        (board['a1'] == board['b2'] == board['c3'] != ' ') or
        (board['c1'] == board['b2'] == board['a3'] != ' ')
    ):
        if turn == "X":
            global o_won, max_wins
            o_won += 1
            print()
            print('O won!')
            print()
            if o_won == max_wins:
                print(f"O won the whole game!")
                sys.exit(0)
        elif turn == "O":
            global x_won
            x_won += 1
            print()
            print('X won!')
            print()
            if x_won == max_wins:
                print(f"X won the whole game!")
                sys.exit(0)
        start_game()
    elif not empty_cells:
        global ties
        ties += 1
        print('Its a tie!')
        start_game()




start_game()