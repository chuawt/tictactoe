from game import TicTacToe, play
from player import RandomComputer, Human, MinimaxComputer

if __name__ == '__main__':
    x_player = Human()
    y_player = MinimaxComputer()
    game = TicTacToe()
    print(play(game, x_player, y_player, print_game=True))