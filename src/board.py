class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            self.board.append([None] * 8) # 8 columns each row

    def place_piece(self, piece, pos):
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
        
        self.board[x, y] = piece

    def remove_piece(self, position):
        x, y = position
        self.board[x, y] = None

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