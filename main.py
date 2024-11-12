from engine import SuperTicTacToe
from ai import MonteCarloAI

def main():
    ask = input("Play with Monte Carlo AI? (y/n): ")
    if ask == 'y' or ask == 'Y':
        game = MonteCarloAI()
        game.play()
    else:
        game = SuperTicTacToe()
        game.play()

if __name__ == '__main__':
    main()