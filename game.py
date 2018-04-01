from string import Template
import board

menu = {}
menu['1'] = "Play"
menu['2'] = "Pause"
menu['3'] = "Quit"


def update_history(board_history, user_board):
    new_board_history = board_history[:]
    new_board_history.append(user_board)
    return new_board_history


def get_coordinate(coord):
    template = Template("Please select $coordinate")
    string = template.substitute(coordinate=coord)
    value = input(string)
    return value if value.isdigit() else get_coordinate(coord)


def apply_coords(x, y, game_board, user_board):
    if game_board[x][y]:
        print("PERDEEEEEEEEEU")
    user_board[x][y] = True
    return user_board

def play(game_board, user_board):
    x = int(get_coordinate("x"))
    y = int(get_coordinate("y"))
    print(x, y)
    if user_board[x][y]:
        print(user_board)
        print("Already tried this position")
        return play(game_board, user_board)
    return apply_coords(x, y, game_board, user_board)


def start():
    game_board = board.create_board(10, 10)
    user_board = board.create_board(10, 10)
    user_board_history = []

    game_board = board.prepare_board(game_board)

    while True:
        options = menu.keys()
        options = sorted(options)
        for entry in options:
            template = Template("$entry - $value")
            string = template.substitute(entry=entry, value=menu[entry])
            print(string)
        selection = input("Please Select2:")
        if selection == '1':
            user_board = play(game_board, user_board)
            user_board_history = update_history(user_board_history, user_board)
        elif selection == '2':
            yield user_board_history
        elif selection == '3':
            yield game_board
        else:
            print("Unknown Option Selected!")
