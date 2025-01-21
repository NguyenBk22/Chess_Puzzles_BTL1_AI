from abc import ABC, abstractmethod

class Pieces:
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def capture(self):
        pass

class King(Pieces):
    def capture(self):
        pass

class Queen(Pieces):
    def capture(self):
        pass

class Knight(Pieces):
    def capture(self):
        pass

class Rook(Pieces):
    def capture(self):
        pass

class Pawn(Pieces):
    def capture(self):
        pass

class Bishop(Pieces):
    def capture(self):
        pass

