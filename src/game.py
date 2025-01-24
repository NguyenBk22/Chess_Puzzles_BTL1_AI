from src.board import Board

class ChessGame:
    def __init__(self):
        self.chess_board = Board()

    def setup_boardgame(self, positions):
        for piece_name, pos in positions:
            self.chess_board.place_piece(piece_name, pos)
        
        return self.chess_board

    def is_win(self):
        numberofpieces = self.chess_board.count_NumberOfPieces()
        if numberofpieces == 1:
            return True
        else:
            return False
