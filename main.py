from src.game import ChessGame
from src.utils import load_initial_position
from src.searching_algorithms.BrFS import brfs
from src.searching_algorithms.Best_First_Search import best_first_search
import copy

def main():
    input_file = "data\\input3.txt"
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
    print("---------- Result of BrFS Algorithm ---------- \n", brfs_result, "\n")

    # Thực hiện Best First Search
    best_first_search_result = best_first_search(game_copy2)
    print("---------- Result of Best First Search Algorithm ---------- \n", best_first_search_result, "\n")

if __name__ == "__main__":
    main()