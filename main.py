from src.game import ChessGame
from src.utils import load_initial_position
# from src.searching_algorithms.BrFS import bfs

def main():
    input_file = "C:\\Python\\Chess_puzzles\\data\\input1.txt"
    positions = load_initial_position(input_file)

    game = ChessGame()
    game.setup_boardgame(positions)
    print(game.chess_board)
    # print(game.chess_board.board)
    print(game.chess_board.get_board_valid_moves())

    # BrFS = 

if __name__ == "__main__":
    main()