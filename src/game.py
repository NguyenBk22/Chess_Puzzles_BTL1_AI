from src.board import Board
import copy

class ChessGame:
    def __init__(self):
        self.chess_board = Board()
        self.parent = None  # Lưu trạng thái cha
        self.move = None    # Lưu nước đi dẫn tới trạng thái này

    def setup_boardgame(self, positions):
        for piece_name, pos in positions:
            self.chess_board.place_piece(piece_name, pos)
        
        return self.chess_board

    def is_goal_state(self):
        numberofpieces = self.chess_board.count_NumberOfPieces()
        if numberofpieces == 1:
            return True
        else:
            return False
        
    def generate_next_states(self):
        list_states = []
        valid_moves = self.chess_board.get_board_valid_moves()
        for valid_move in valid_moves:
            new_game_state = copy.deepcopy(self)
            new_game_state.chess_board.update_board(valid_move)
            new_game_state.parent = self  # Ghi lại trạng thái cha
            new_game_state.move = valid_move  # Ghi lại nước đi
            list_states.append(new_game_state)

        return list_states