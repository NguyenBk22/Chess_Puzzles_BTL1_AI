from src.game import ChessGame
from src.utils import load_initial_position
from src.searching_algorithms.BrFS import brfs
from src.searching_algorithms.Hill_Climbing import hill_climbing
import copy

def main():
    input_file = "C:\\Python\\Chess_puzzles\\data\\input4.txt"
    positions = load_initial_position(input_file)

    game = ChessGame()
    game.setup_boardgame(positions)

    #TEST
    print("----------- Initial Board ---------- \n", game.chess_board, "\n")
    # print(game.chess_board.board)
    print("---------- Valid Moves ---------- \n", game.chess_board.get_board_valid_moves(), "\n")

    # Khởi tạo nhiều đối tượng board
    game_copy1 = copy.deepcopy(game)
    game_copy2 = copy.deepcopy(game)

    # Thực hiện BrFS
    brfs_result = brfs(game_copy1)
    print("---------- Result ---------- \n", brfs_result, "\n")

    # Thực hiện Hill Climbing
    # hill_climbing_result = hill_climbing(game_copy2)

if __name__ == "__main__":
    main()