# implementing the monte carlo method

import random
import math
from engine import SuperTicTacToe

class MonteCarloAI:
    def __init__(self):
        self.iter = 500
        self.game = SuperTicTacToe()
        self.board = self.game.board
        self.turn = False

    def get_best_move(self):
        """
        Returns the best move based on Monte Carlo simulation results
        """
        pass
        #return a, b

    def _simulate_game(self):
        """
        Simulates a random game from the current position until completion
        Returns the winner ('X', 'O', or 'Draw')
        """

    def get_move(self):
        if self.turn:
            return self.get_best_move()  # Automatically generate an AI move
        else:
            return self.game.get_valid_move()  # Manual input for human player
