import random
import math

import logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s %(levelname)s: %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S')
                    

class Player:
    def __init__(self):
        # Marker is 'X' or 'O'
        self.marker = ''
        self.opponent = None  # use for MinimaxComputer


    def __repr__(self):
       return (f'{self.__class__.__name__}')
    

    def get_move(self, game):
        pass


class RandomComputer(Player):
    def __init__(self):
        super().__init__()


    def get_move(self, game):
        """ Randomly choose a valid spot as next move. """
        return random.choice(game.available_moves())


class Human(Player):
    def __init__(self):
        super().__init__()


    def get_move(self, game):
        """ Ask user for the next move. """
        valid_move = False
        while not valid_move:
            move = input(f'{self.marker}\'s turn. Input move (1-9): ')
            try:
                move = int(move)-1
                if move not in game.available_moves():
                    raise ValueError
                # Otherwise move is valid
                valid_move = True
            except ValueError:
                print('Invalid square. Try again.')
        return move


class MinimaxComputer(Player):
    def __init__(self):
        super().__init__()


    def get_move(self, game):
        """ Calculate the best move based on the minimax algorithm. """
        # If start first, choose a random move.
        if game.num_available_moves() == 9:
            move = random.choice(game.available_moves())
        else:
            # Get move based on the minimax algorithm
            move = self.minimax(game, depth=1, is_max=True)
        return move['position']

    
    def minimax(self, state, depth, is_max):

        # Set a utility score of 10 for a win, -10 for a lose, 0 for draw.
        # Adjust the utility score with the depth of the decision tree, 
        # to penalize positions that take longer to win.
        if state.check_winner(self):
            return {'score': 10 - depth, 'position': None}
        elif state.check_winner(self.opponent):
            return {'score': -10 + depth, 'position': None}
        elif state.game_draw():
            return {'score': 0, 'position': None}

        # If this is maximizer's move
        if is_max:
            best = {'score': -math.inf, 'position': None}
            for move in state.available_moves():
                state.valid_move(move, self)
                score = self.minimax(state, depth+1, is_max=False)['score']
                if score > best['score']:
                    best = {'score': score, 'position': move}
                # Undo move
                state.board[move] = ''
            return best
        else:
            best = {'score': math.inf, 'position': None}
            for move in state.available_moves():
                state.valid_move(move, self.opponent)
                score = self.minimax(state, depth+1, is_max=True)['score']
                if score < best['score']:
                    best = {'score': score, 'position': move}
                # Undo move
                state.board[move] = ''
            return best
        
            


