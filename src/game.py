from src.board import Board

class ChessGame:
    def __init__(self):
        self.board = Board()

    def setup_boardgame(self, positions):
        for piece_name, pos in positions:
            self.board.place_piece(piece_name, pos)
        
        return self.board

    def is_win(self):
        numberofpieces = self.board.count_NumberOfPieces()
        if numberofpieces == 1:
            return True
        else:
            return False