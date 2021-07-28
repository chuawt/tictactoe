import random
import math
                    

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
        """ Return a dictionary containing the best move position and its score.
        
        dictionary keys:
        'score': (int) adjusted utility score of the best move for MinimaxComputer
        'position': (int, 1-9) the best move on the tictactoe board
        """
        # Define terminal states.
        # Set a utility score of 10 (max depth + 1) for a win, -10 for a lose, 0 for draw.
        # Subtract the depth of the decision tree from the utility score 
        # to penalize positions that take longer to win.
        if state.check_winner(self):
            return {'score': 10 - depth, 'position': None}
        elif state.check_winner(self.opponent):
            return {'score': -(10 - depth), 'position': None}
        elif state.game_draw():
            return {'score': 0, 'position': None}

        # Initalize best move.
        if is_max:
            best = {'score': -math.inf, 'position': None}  # any move will have a higher score for maximizer
            # Make all possible move for maximizer.
            for move in state.available_moves():
                state.valid_move(move, self)
                # Swap players and call minimax function recursively.
                score = self.minimax(state, depth+1, is_max=False)['score']
                # Update dictionary if current move has a higher score.
                if score > best['score']:
                    best = {'score': score, 'position': move}
                # Undo move.
                state.board[move] = ''
        else:
            best = {'score': math.inf, 'position': None}  # any move will have a lower score for minimizer
            # Make all possible move for minimizer.
            for move in state.available_moves():
                state.valid_move(move, self.opponent)
                # Swap players and call minimax function recursively.
                score = self.minimax(state, depth+1, is_max=True)['score']
                # Update dictionary if current move has a lower score.
                if score < best['score']:
                    best = {'score': score, 'position': move}
                # Undo move.
                state.board[move] = ''
        return best