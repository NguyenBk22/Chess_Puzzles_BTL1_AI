from abc import ABC, abstractmethod

class Pieces:
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def get_valid_moves(self, board):
        pass

    @abstractmethod
    def __str__(self):
        pass

class King(Pieces):
    def get_valid_moves(self, board):
        valid_moves = []
        x, y = self.position
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:  # Trong bàn cờ
                if board[nx][ny] is not None:  # Ô chứa quân khác
                    valid_moves.append((nx, ny))
        return valid_moves

    def __str__(self):
        return "K"

class Queen(Pieces):
    def get_valid_moves(self, board):
        valid_moves = []
        x, y = self.position
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx][ny] is not None:  # Gặp quân khác
                    valid_moves.append((nx, ny))
                    break  # Chỉ ăn quân và dừng
                nx += dx
                ny += dy
        return valid_moves

    def __str__(self):
        return "Q"

class Rook(Pieces):
    def get_valid_moves(self, board):
        valid_moves = []
        x, y = self.position
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx][ny] is not None:
                    valid_moves.append((nx, ny))
                    break
                nx += dx
                ny += dy
        return valid_moves

    def __str__(self):
        return "R"

class Bishop(Pieces):
    def get_valid_moves(self, board):
        valid_moves = []
        x, y = self.position
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx][ny] is not None:
                    valid_moves.append((nx, ny))
                    break
                nx += dx
                ny += dy
        return valid_moves

    def __str__(self):
        return "B"

class Knight(Pieces):
    def get_valid_moves(self, board):
        valid_moves = []
        x, y = self.position
        jumps = [
            (-2, -1), (-2, 1), (2, -1), (2, 1),
            (-1, -2), (-1, 2), (1, -2), (1, 2)
        ]
        for dx, dy in jumps:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx][ny] is not None:
                    valid_moves.append((nx, ny))
        return valid_moves

    def __str__(self):
        return "N"

class Pawn(Pieces):
    def get_valid_moves(self, board):
        valid_moves = []
        x = self.position[0]
        y = self.position[1]
        
        # Di chuyển chéo trái nếu ăn quân
        if x > 0 and y > 0 and board[x - 1][y - 1] is not None:
            valid_moves.append((x - 1, y - 1))

        # Di chuyển chéo phải nếu ăn quân
        if x > 0 and y < 7 and board[x - 1][y + 1] is not None:
            valid_moves.append((x - 1, y + 1))
            
        return valid_moves

    def __str__(self):
        return "P"