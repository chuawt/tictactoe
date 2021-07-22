from math import log
from player import RandomComputer, Human

class TicTacToe:
    def __init__(self):
        # Use a list to represent the 3x3 board
        self.board = ['' for _ in range(9)]
        self.current_winner = None


    def __repr__(self):
       return (f'{self.__class__.__name__}')


    def __str__(self):
        """ Create a string representation of current board. """
        return '''
            \t {} | {} | {}
            \t-----------
            \t {} | {} | {}
            \t-----------
            \t {} | {} | {}
        '''.format(*[i+1 if spot == '' else spot for i, spot in enumerate(self.board)])


    def available_moves(self):
        """ Return a list of available moves by their indexes. """
        return [i for i, spot in enumerate(self.board) if spot == '']


    def num_available_moves(self):
        """ Return the number of available moves remaining. """
        return len(self.available_moves())


    def game_draw(self):
        """ Return True if game is a tie, and False otherwise. """
        return self.num_available_moves() == 0


    def check_winner(self, player):
        """ Modify `self.current_winner` if there is a winner.
            Return True if there is a winner, and False otherwise. """
        WIN_SEQUENCES = [[0,1,2], [3,4,5], [6,7,8],
                         [0,3,6], [1,4,7], [2,5,8],
                         [0,4,8], [2,4,6]]
        for seq in WIN_SEQUENCES:
            if all(self.board[idx] == player.marker for idx in seq):
                self.current_winner = player
                return True
        return False
        

    def valid_move(self, move, player):
        """ Modify `self.board` with the move and marker. 
        Return True if move is valid, and False otherwise. """
        if self.board[move] == '':
            self.board[move] = player.marker
            return True
        return False


def play(game, x_player, o_player, print_game=True):
    """ Returns 1 if x_player wins, -1 if o_player wins, and 0 for a tie. """
    if print_game:
        print(game)

    x_player.marker = 'x'
    o_player.marker = 'o'
    current_player = x_player  # start with x_player

    while not game.game_draw():
        # Get the move from the appropriate player
        move = current_player.get_move(game)

        if game.valid_move(move, current_player):
            if print_game:
                print(f'{current_player.marker} makes a move to square {move+1}.')
                print(game)
            
            # Check if current board has a winner
            game.check_winner(current_player)
            
            if game.current_winner:
                if print_game:
                     print(f'{current_player.marker} wins!')
                return 1 if current_player == x_player else -1

            # Switch players
            if current_player == x_player:
                current_player = o_player
            else: 
                current_player = x_player
    
    # Exit while loop means it is a draw game.
    if print_game:
        print('It\'s a tie!')
    return 0    


if __name__ == '__main__':
    x_player = Human()
    y_player = Human()
    game = TicTacToe()
    print(play(game, x_player, y_player, print_game=True))