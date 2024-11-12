import numpy as np
import random
import math
from copy import deepcopy
from engine import SuperTicTacToe

class MonteCarloAI(SuperTicTacToe):
    def __init__(self, iter=500):    
        """
        Play with a Monte Carlo AI player for the Super TicTacToe game.
        
        Parameters:
            iter (int): The number of iterations for the Monte Carlo simulation.

        """
        super().__init__()
        self.iter = iter

    def get_best_move(self, player):
        """
        Returns the best move based on Monte Carlo simulation results
        Returns: tuple (row, col) representing the best move
        """
        available_moves = [(i,j) for i in range(9) for j in range(9) if self.board[i].board[j] == " "]

        # store wins for each possible move
        wins = {move: 0 for move in available_moves}
        sims = {move: 0 for move in available_moves}

        for move in available_moves:
            for _ in range(self.iter):
                board_copy = deepcopy(self.board)

                board_copy[move[0]].board[move[1]] = player

                temp_game = SuperTicTacToe()
                temp_game.board = board_copy
                result = temp_game._simulate_game()

                if result == player:
                    wins[move] += 1
                sims[move] += 1

        move_win_rates = {move: wins[move]/sims[move] for move in available_moves}

        return max(move_win_rates, key=move_win_rates.get)

    def _simulate_game(self):
        """
        Simulates a random game from the current position until completion
        Returns the winner ('X', 'O', or 'Draw')
        """
        pass

    def play(self):
        self.display() 
        player = "O"
        
        while True:
            if player == "O":
                a, b = self.get_valid_move(player) 
            else:
                a, b = self.get_best_move(player)
            
            mini_board = self.board[a]
            mini_board.play(player, b)

            if mini_board.check_win():
                self.meta_board[a] = player
                mini_board.board = np.full(9, player)
                self.next_board = "any"
            elif mini_board.check_draw():
                self.meta_board[a] = "D"
                mini_board.board = np.full(9, "D")
                self.next_board = "any"

            if self.check_win():
                self.display() 
                print(f"player '{player}' won the game!") 
            
            if self.check_draw():
                self.display() 
                print("Draw") 

            if player == "O":
                player = "X"
            else:
                player = "O"
            
            self.display() 
        
