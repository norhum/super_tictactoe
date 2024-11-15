import pygame

WIDTH, HEIGHT = 300, 300
SQUARE_SIZE = 100
ROWS, COLS = 3, 3

class TicTacToe:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic-Tac-Toe")
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.current_player = 'X'

    def draw_board(self):
        self.screen.fill((28, 170, 156))
        for x in range(SQUARE_SIZE, WIDTH, SQUARE_SIZE):
            pygame.draw.line(self.screen, (23, 145, 135), (x, 0), (x, HEIGHT), 5)
        for y in range(SQUARE_SIZE, HEIGHT, SQUARE_SIZE):
            pygame.draw.line(self.screen, (23, 145, 135), (0, y), (WIDTH, y), 5)
        self.draw_figures()
        pygame.display.flip()

    def draw_figures(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 'X':
                    self.draw_x(row, col)
                elif self.board[row][col] == 'O':
                    self.draw_o(row, col)

    def draw_x(self, row, col):
        x1 = col * SQUARE_SIZE + 15
        y1 = row * SQUARE_SIZE + 15
        x2 = (col + 1) * SQUARE_SIZE - 15
        y2 = (row + 1) * SQUARE_SIZE - 15
        pygame.draw.line(self.screen, (68, 70, 156), (x1, y1), (x2, y2), 15)
        pygame.draw.line(self.screen, (68, 70, 156), (x2, y1), (x1, y2), 15)

    def draw_o(self, row, col):
        center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
        center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2
        pygame.draw.circle(self.screen, (242, 85, 96), (center_x, center_y), SQUARE_SIZE // 2 - 15, 15)

    def handle_click(self, pos):
        row = pos[1] // SQUARE_SIZE
        col = pos[0] // SQUARE_SIZE
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.draw_board()
            if self.check_winner():
                print(f"{self.check_winner()} wins!")
                self.reset_board()

    def check_winner(self):
        # Check rows and columns
        for i in range(ROWS):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                return self.board[0][i]
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2]
        return None

    def reset_board(self):
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.current_player = 'X'
        self.draw_board()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)
            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()