from string import Template
import game

menu = {}
menu['1'] = "New game"
menu['2'] = "Continue"
menu['3'] = "Quit"


def print_options():
    options = menu.keys()
    options = sorted(options)
    for entry in options:
        template = Template("$entry - $value")
        string = template.substitute(entry=entry, value=menu[entry])
        print(string)


def run():
    board_iterator = None
    board_history = []
    while True:
        print_options()
        selection = input("Please Select:")
        if selection == '1':
            board_iterator = iter(game.start())
            board_history = next(board_iterator)
            print(board_history[-1:])
        elif selection == '2':
            board_history = next(board_iterator)
            print(board_history[-1:])
        elif selection == '3':
            print(board_history)
            break
        else:
            print("Unknown Option Selected!")
