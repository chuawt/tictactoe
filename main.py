from game import TicTacToe, play
from player import RandomComputer, Human

if __name__ == '__main__':
    x_player = Human()
    y_player = Human()
    game = TicTacToe()
    print(play(game, x_player, y_player, print_game=True))