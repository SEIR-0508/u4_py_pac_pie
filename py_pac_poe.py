state = {}


def play():

    print("----------------------")
    print("Let's play Py-Pac-Poe!")
    print("----------------------")

    state["board"] = {
        'a1': ' ', 'b1': ' ', 'c1': ' ',
        'a2': ' ', 'b2': ' ', 'c2': ' ',
        'a3': ' ', 'b3': ' ', 'c3': ' ',
    }

    state["turn"] = 'X'
    state["winner"] = ''

    def print_board():
        print("------------------------------")
        print("                              ")
        print("    A   B   C")
        print(
            f"1)  {state['board']['a1']} | {state['board']['b1']} | {state['board']['c1']} ")
        print("  ------------")
        print(
            f"2)  {state['board']['a2']} | {state['board']['b2']} | {state['board']['c2']} ")
        print("  ------------")
        print(
            f"3)  {state['board']['a3']} | {state['board']['b3']} | {state['board']['c3']} ")
        print("                              ")
        print("------------------------------")

    while state["winner"] == '':

        print_board()

        need_valid_move = True

        while need_valid_move:
            print(f"Player {state['turn']}'s to move (example B2):")
            location = input().lower()
            for key in state["board"]:
                if key == location and state["board"][key] == ' ':
                    need_valid_move = False
                    break

            if need_valid_move:
                print("invalid move")

        state["board"][location] = state["turn"]

        if state["board"]["b2"] != ' ' and ((state["board"]["a1"] == state["board"]["b2"] == state["board"]["c3"]) or (state["board"]["a2"] == state["board"]["b2"] == state["board"]["c2"]) or (state["board"]["a3"] == state["board"]["b2"] == state["board"]["c1"]) or (state["board"]["b1"] == state["board"]["b2"] == state["board"]["b3"])):
            state["winner"] = state["board"]["b2"]

        elif state["board"]["a1"] != ' ' and ((state["board"]["a1"] == state["board"]["a2"] == state["board"]["a3"]) or (state["board"]["a1"] == state["board"]["b1"] == state["board"]["c1"])):
            state["winner"] = state["board"]["a1"]

        elif state["board"]["c3"] != ' ' and ((state["board"]["a3"] == state["board"]["b3"] == state["board"]["c3"]) or (state["board"]["c1"] == state["board"]["c2"] == state["board"]["c3"])):
            state["winner"] = state["board"]["c3"]

        tie_game = True
        for key in state["board"]:
            if state["board"][key] == ' ':
                tie_game = False
        if tie_game:
            state["winner"] = "tie"

        state["turn"] = "O" if state["turn"] == "X" else "X"

    print_board()
    if state["winner"] == 'tie':
        print('Tie Game!')
    else:
        print(f'{state["winner"]} wins the game!')

    print("play again? y/n")
    decision = input().lower()

    if decision == "y":
        play()
    else:
        print("goodbye")


play()
