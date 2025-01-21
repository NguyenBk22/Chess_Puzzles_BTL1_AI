from src.game import ChessGame
from src.utils import load_initial_position

def main():
    input_file = ""
    positions = load_initial_position(input_file)

    game = ChessGame()
    game.setup_boardgame(positions)

    while not game.is_win():
        #Logic xử lý
        pass

if __name__ == "__main__":
    main()