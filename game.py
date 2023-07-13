spaces = {"a1": " ",
          "a2": " ",
          "a3": " ",
          "b1": " ",
          "b2": " ",
          "b3": " ",
          "c1": " ",
          "c2": " ",
          "c3": " "}

board = []


def define_board():
    global board
    board = ["     A   B   C", f" 1)  {spaces['a1']} | {spaces['b1']} | {spaces['c1']} ", "    -----------",
             f" 2)  {spaces['a2']} | {spaces['b2']} | {spaces['c2']} ", "    -----------", f" 3)  {spaces['a3']} | {spaces['b3']} | {spaces['c3']} "]


x_turn = True


def welcome_message():
    print("----------------------")
    print(" Let's play Py-Pac-Poe! ")
    print("----------------------")


def print_board():
    for line in board:
        print(line)


def reset_game():
    global spaces
    spaces = {"a1": " ",
              "a2": " ",
              "a3": " ",
              "b1": " ",
              "b2": " ",
              "b3": " ",
              "c1": " ",
              "c2": " ",
              "c3": " "}
    define_board()


def check_winner():
    if spaces['a1'] == spaces['b1'] == spaces['c1'] and spaces['a1'] != " ":
        return spaces['a1']
    elif spaces['a2'] == spaces['b2'] == spaces['c2'] and spaces['a2'] != " ":
        return spaces['a2']
    elif spaces['a3'] == spaces['b3'] == spaces['c3'] and spaces['a3'] != " ":
        return spaces['a3']
    elif spaces['a1'] == spaces['a2'] == spaces['a3'] and spaces['a1'] != " ":
        return spaces['a1']
    elif spaces['b1'] == spaces['b2'] == spaces['b3'] and spaces['b1'] != " ":
        return spaces['b1']
    elif spaces['c1'] == spaces['c2'] == spaces['c3'] and spaces['c1'] != " ":
        return spaces['c1']
    elif spaces['a1'] == spaces['b2'] == spaces['c3'] and spaces['c3'] != " ":
        return spaces['a1']
    elif spaces['a3'] == spaces['b2'] == spaces['c1'] and spaces['a3'] != " ":
        return spaces['a3']
    else:
        return False


def init_turn():
    global spaces, x_turn
    check_winner_result = check_winner()
    if check_winner_result:
        print_board()
        inp = input(
            f'Player {check_winner_result} wins!! Play again (Y/N): ').lower()
        if inp == 'y':
            reset_game()
            init_game()

    if x_turn:
        print_board()
        inp = input("Player X's Move (example B2): ").lower()
        if spaces[inp] == " ":
            spaces[inp] = "X"
            x_turn = False
        else:
            print('Bogus move! Try again...')
            init_turn()
        define_board()
        init_turn()
    if not x_turn:
        print_board()
        inp = input("Player O's Move (example B2): ").lower()
        if spaces[inp] == " ":
            spaces[inp] = "O"
            x_turn = True
        else:
            print('Bogus move! Try again...')
            init_turn()
        define_board()
        init_turn()


def init_game():
    welcome_message()
    define_board()
    init_turn()


init_game()
