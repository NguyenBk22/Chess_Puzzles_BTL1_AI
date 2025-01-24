from src.game import ChessGame
from src.utils import load_initial_position

def main():
    input_file = "C:\\Python\\Chess_puzzles\\data\\input1.txt"
    positions = load_initial_position(input_file)

    game = ChessGame()
    board = game.setup_boardgame(positions)
    print(board)
    
    while not game.is_win():
        #Logic xử lý giải thuật tìm kiếm
        break

if __name__ == "__main__":
    main()