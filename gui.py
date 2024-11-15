import tkinter as tk
from engine import SuperTicTacToe
from ai import MonteCarloAI

class SuperTicTacToeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Super Tic Tac Toe")
        self.geometry("600x600")

        self.game = SuperTicTacToe()
        self.buttons = []
        self.create_board()

        self.player = "O"
        self.human_turn = True

        self.play_button = tk.Button(self, text="Play", command=self.play)
        self.play_button.grid(row=3, column=1, pady=10)

    def create_board(self):
        for i in range(9):
            row = i // 3
            col = i % 3
            button = tk.Button(self, text="", width=6, height=3, command=lambda x=i: self.handle_click(x))
            button.grid(row=row, column=col)
            self.buttons.append(button)

    def handle_click(self, position):
        if self.human_turn:
            row, col = divmod(position, 3)
            self.game.board[row][col].play(self.player, col)
            self.update_board()

            if self.game.check_win():
                self.display_winner(self.player)
                return
            if self.game.check_draw():
                self.display_winner("Draw")
                return

            self.player = "O" if self.player == "X" else "X"
            self.human_turn = False
            self.after(500, self.ai_turn)

    def ai_turn(self):
        row, col = self.game.get_best_move(self.player)
        self.game.board[row][col].play(self.player, col)
        self.update_board()

        if self.game.check_win():
            self.display_winner(self.player)
            return
        if self.game.check_draw():
            self.display_winner("Draw")
            return

        self.player = "O" if self.player == "X" else "X"
        self.human_turn = True

    def update_board(self):
        for i in range(9):
            row = i // 3
            col = i % 3
            if self.game.board[row][col].board[col] == "X":
                self.buttons[i].config(text="X", bg="lightgreen")
            elif self.game.board[row][col].board[col] == "O":
                self.buttons[i].config(text="O", bg="lightblue")
            else:
                self.buttons[i].config(text="", bg="white")

    def display_winner(self, winner):
        if winner == "Draw":
            message = "It's a draw!"
        else:
            message = f"Player '{winner}' wins!"
        tk.messagebox.showinfo("Game Over", message)
        self.game = SuperTicTacToe()
        self.update_board()

    def play(self):
        self.human_turn = True
        self.player = "O"
        self.game = SuperTicTacToe()
        self.update_board()

if __name__ == "__main__":
    app = SuperTicTacToeGUI()
    app.mainloop()