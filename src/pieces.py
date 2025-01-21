from abc import ABC, abstractmethod

class Pieces:
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def capture(self, board):
        pass

class King(Pieces):
    def capture(self, board):
        valid_moves = []
        x = self.position[0]
        y = self.position[1]

        #Straight Moves
        if board[x - 1][y] != None and 1 <= x <= 7:
            valid_moves += [(x - 1, y)]

        #Back Moves
        if board[x + 1][y] != None and 0 <= x <= 6:
            valid_moves += [(x + 1, y)]

        #Right Moves
        if board[x][y + 1] != None and 0 <= y <= 6:
            valid_moves += [(x, y + 1)]

        #Left Moves
        if board[x][y - 1] != None and 1 <= y <= 7:
            valid_moves += [(x, y - 1)]

        #Straight Right Moves
        if board[x - 1][y + 1] != None and 1 <= x <= 7 and 0 <= y <= 6:
            valid_moves += [(x - 1, y + 1)]

        #Straight Left Moves
        if board[x - 1][y - 1] != None and 1 <= x <= 7 and 1 <= y <= 7:
            valid_moves += [(x - 1, y - 1)]
        
        #Back Right Moves
        if board[x + 1][y + 1] != None and 0 <= x <= 6 and 0 <= y <= 6:
            valid_moves += [(x + 1, y + 1)]
        
        #Back Left Moves
        if board[x + 1][y - 1] != None and 0 <= x <= 6 and 1 <= y <= 7:
            valid_moves += [(x + 1, y - 1)] 

        return valid_moves
            
class Queen(Pieces):
    def capture(self, board):
        valid_moves = []
        x = self.position[0]
        y = self.position[1]

        #Straight Moves
        for i in range(x, -1, -1):
            if board[i][y] != None:
                valid_moves += [(i, y)]
                break

        #Back Moves
        for i in range(x, 8, 1):
            if board[i][y] != None:
                valid_moves += [(i, y)]
                break

        #Right Moves
        for i in range(y, 8, 1):
            if board[x][i] != None:
                valid_moves += [(x, i)]
                break

        #Left Moves
        for i in range(y, -1, -1):
            if board[x][i] != None:
                valid_moves += [(x, i)]
                break

        #Straight Right Moves
        i = x - 1
        j = y + 1

        while i >= 0 and j < 8:
            if board[i][j] != None:
                valid_moves += [(i, j)]
                break
            i -= 1
            j += 1
            
        #Straight Left Moves
        i = x - 1
        j = y - 1
        while i >= 0 and j >= 0:
            if board[i][j] != None:
                valid_moves += [(i, j)]
                break
            i -= 1
            j -= 1

        #Back Right Moves
        i = x + 1
        j = y + 1
        while i < 8 and j < 8:
            if board[i][j] != None:
                valid_moves += [(i, j)]
                break
            i += 1
            j += 1

        #Back Left Moves
        i = x + 1
        j = y - 1
        while i < 8 and j >= 0:
            if board[i][j] != None:
                valid_moves += [(i, j)]
                break
            i += 1
            j -= 1

        return valid_moves
            
class Knight(Pieces):
    def capture(self, board):
        valid_moves = []
        x = self.position[0]
        y = self.position[1]

        moves = [
            (-2, -1), (-2, 1), 
            (2, -1), (2, 1), 
            (-1, -2), (1, -2), 
            (-1, 2), (1, 2)
        ]
        
        for dx, dy in moves:
            x_new = x + dx
            y_new = y + dy

            if 0 <= x_new <= 7 and 0 <= y_new <= 7 and board[x_new][y_new] != None:
                valid_moves += [(x_new, y_new)]
                
        return valid_moves

class Rook(Pieces):
    def capture(self, board):
        valid_moves = []
        x = self.position[0]
        y = self.position[1]

        #Straight Moves
        for i in range(x, -1, -1):
            if board[i][y] != None:
                valid_moves += [(i, y)]
                break

        #Back Moves
        for i in range(x, 8, 1):
            if board[i][y] != None:
                valid_moves += [(i, y)]
                break

        #Right Moves
        for i in range(y, 8, 1):
            if board[x][i] != None:
                valid_moves += [(x, i)]
                break

        #Left Moves
        for i in range(y, -1, -1):
            if board[x][i] != None:
                valid_moves += [(x, i)]
                break
        
        return valid_moves

class Pawn(Pieces):
    def capture(self, board):
        valid_moves = []
        x = self.position[0]
        y = self.position[1]
    
        if board[x - 1][y - 1] != None and 1 <= x <= 7 and 1 <= y <= 7:
            valid_moves += [(x - 1, y - 1)]
        if board[x - 1][y + 1] != None and 1 <= x <= 7 and 0 <= y <= 6:
            valid_moves  += [(x - 1, y + 1)]
        
        return valid_moves

class Bishop(Pieces):
    def capture(self, board):
        valid_moves = []
        x = self.position[0]
        y = self.position[1]
        
        #Straight Right Moves
        i = x - 1
        j = y + 1

        while i >= 0 and j < 8:
            if board[i][j] != None:
                valid_moves += [(i, j)]
                break
            i -= 1
            j += 1
            
        #Straight Left Moves
        i = x - 1
        j = y - 1
        while i >= 0 and j >= 0:
            if board[i][j] != None:
                valid_moves += [(i, j)]
                break
            i -= 1
            j -= 1

        #Back Right Moves
        i = x + 1
        j = y + 1
        while i < 8 and j < 8:
            if board[i][j] != None:
                valid_moves += [(i, j)]
                break
            i += 1
            j += 1

        #Back Left Moves
        i = x + 1
        j = y - 1
        while i < 8 and j >= 0:
            if board[i][j] != None:
                valid_moves += [(i, j)]
                break
            i += 1
            j -= 1

        return valid_moves
