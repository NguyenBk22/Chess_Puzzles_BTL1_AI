from pieces import King, Knight, Queen, Pawn, Rook, Bishop

class Board:
    def __init__(self):
        self.piece = {
            'K': King,
            'Q': Queen,
            'N': Knight,
            'P': Pawn,
            'R': Rook,
            'B': Bishop,
        }
        self.board = []
        for i in range(8):
            self.board.append([None] * 8) # 8 columns each row

    def convert_valid_position(self, pos):
        x = 8 - pos[1]
        y = pos[0]
        if y == 'a':
            y = 0
        elif y == 'b':
            y = 1
        elif y == 'c':
            y = 2
        elif y == 'd':
            y = 3
        elif y == 'e':
            y = 4
        elif y == 'f':
            y = 5
        elif y == 'g':
            y = 6
        elif y == 'h':
            y = 7
        else:
            return "This is invalid position"
        return x, y
    
    def place_piece(self, piece_name, pos):
        x, y = self.convert_valid_position(pos)
        # Kiểm tra x, y có nằm trong phạm vi bàn cờ
        if not (0 <= x < 8 and 0 <= y < 8):
            return "Position out of bounds"
        
        piece_upper = piece_name.upper()
        
        if piece_upper in self.piece:
            self.board[x][y] = self.piece[piece_upper]([x, y])
        else:
            return "Invalid Piece"

    def remove_piece(self, pos):
        x, y = self.convert_valid_position(pos)
        self.board[x][y] = None

    def is_valid_move(self, piece, new_position):
        if new_position == None:
            return False
        else:
            return True
        
    def count_NumberOfPieces(self):
        cnt = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != None:
                    cnt += 1
        return cnt