import random

class Player:
    def __init__(self):
        # Marker is 'X' or 'O'
        self.marker = ''


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