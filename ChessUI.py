import pygame
import os
import time  # Import time for delays
from src.game import ChessGame
from src.utils import load_initial_position
from src.searching_algorithms.BrFS import brfs
from src.searching_algorithms.Best_First_Search import best_first_search
import random

# Constants
BOARD_SIZE = 8
CELL_SIZE = 80  # Each square size
MARGIN = 20  # Margin around the board for the white edge
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BOARD_X = MARGIN  # X position for the chessboard
BOARD_Y = MARGIN  # Y position for the chessboard
MAX_PIECES = 6

# Colors
LIGHT_SQUARE = (240, 217, 181)  # Light Beige
DARK_SQUARE = (181, 136, 99)    # Brown
HIGHLIGHT_COLOR = (193, 247, 150)  # Light Green
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()

# Set up display
WINDOW_WIDTH = BOARD_SIZE * CELL_SIZE + 250
WINDOW_HEIGHT = BOARD_SIZE * CELL_SIZE + 50
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Chess Ranger")




def generate_random_chess_input(filename="data/input_random.txt"):
    pieces = ["K", "Q", "R", "B", "N", "P"]  # White chess pieces
    board_positions = set()  # Track occupied positions
    notation_list = []  # Stores tuples in (piece, position) format

    def random_square():
        """Generate a random chessboard square (e.g., 'e4', 'd6')."""
        return f"{random.choice('abcdefgh')}{random.randint(1, 8)}"

    while True:  # Keep generating until a solvable board is found
        board_positions.clear()
        notation_list.clear()

        num_pieces = random.randint(2, MAX_PIECES)
        
        for _ in range(num_pieces):
            piece = random.choice(pieces)  # Pick a random piece
            placed = False

            while not placed:
                square = random_square()
                if square not in board_positions:  # Avoid duplicate placements
                    board_positions.add(square)
                    notation_list.append((piece, square))  # Store as tuple (piece, position)
                    placed = True

        # Load this board into the game without saving
        game = ChessGame()
        game.setup_boardgame(notation_list)  # Directly load (piece, pos) tuples

        if best_first_search(game) != ([], []):  # Check if BFS finds a solution
            # Now save the board since it's solvable
            with open(filename, "w") as f:
                for piece, pos in notation_list:
                    f.write(f"{piece}{pos}\n")  # Example: "Qd6"

            return filename  # Return list of (piece, position) tuples
        

# Load images
def load_piece_images():
    pieces = ["king", "queen", "rook", "bishop", "knight", "pawn"]
    images = {}

    for piece in pieces:
        filename = f"src/images/white-{piece}.png"
        if os.path.exists(filename):
            img = pygame.image.load(filename)
            img = pygame.transform.scale(img, (CELL_SIZE - 10, CELL_SIZE - 10))
            images[piece] = img
        else:
            print(f"Warning: Missing image {filename}")

    return images


piece_images = load_piece_images()

# Mapping chess notation to image names
piece_map = {
    "K": "king",
    "Q": "queen",
    "R": "rook",
    "B": "bishop",
    "N": "knight",
    "P": "pawn"
}

class ChessPygame:
    def __init__(self, filename = "data\\input_random.txt"):
        if filename == "data\\input_random.txt":
            new_game_filename = generate_random_chess_input()
            self.load_game(new_game_filename)
        self.load_game(filename)
        
        self.brfs_visited = []
        self.brfs_index = 0
        self.brfs = False
        
        self.bfs_visited = []
        self.bfs_index = 0
        self.bfs = False
         # Animation state
        self.animation_time = 500  # Time for one move animation in milliseconds
        self.animation_start_time = 0
        self.animation_running = False
        self.start_pos = None
        self.end_pos = None
        self.input=filename
        
        
    def load_game(self, filename):
        """Load a new chess game from file."""
        self.input = filename
        self.initial_positions = load_initial_position(filename)
        self.game = ChessGame()
        self.game.setup_boardgame(self.initial_positions)
        
        self.solution_moves = []
        self.step_index = 0
        
        self.brfs_visited = []
        self.brfs_index = 0
        self.brfs = False
        
        self.bfs_visited = []
        self.bfs_index = 0
        self.bfs = False


    def draw_board(self):
        """Draw the chessboard with alternating colors and coordinates."""
        font = pygame.font.SysFont("Arial", 24, bold=True)
        letters = "abcdefgh"

        # Draw white edge around the board (without top margin)
        # This will remove the white edge above the chessboard
        pygame.draw.rect(screen, WHITE, (BOARD_X - MARGIN, BOARD_Y - MARGIN, 
                                        BOARD_SIZE * CELL_SIZE + MARGIN * 2, 
                                        BOARD_SIZE * CELL_SIZE + MARGIN))  # No top margin

        # Draw board squares with alternating colors
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x = BOARD_X + col * CELL_SIZE
                y = BOARD_Y + row * CELL_SIZE

                # Choose color based on position
                color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
                pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

        # Draw coordinates (numbers on the left, letters on the bottom)
        # Numbers (1-8) placed on the left side of the chessboard
        for row in range(BOARD_SIZE):
            number_text = font.render(str(8 - row), True, BLACK)
            screen.blit(number_text, (BOARD_X - MARGIN, BOARD_Y + row * CELL_SIZE + CELL_SIZE // 2 - number_text.get_height() // 2))

        # Letters (a-h) placed **below** the chessboard
        for col in range(BOARD_SIZE):
            letter_text = font.render(letters[col], True, BLACK)
            screen.blit(letter_text, (BOARD_X + col * CELL_SIZE + CELL_SIZE // 2 - letter_text.get_width() // 2,
                                    BOARD_Y + BOARD_SIZE * CELL_SIZE + 5))  # Adjusted the margin for letters

    def draw_pieces(self, chess_game):
        """Draw pieces at their current positions."""
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                piece = chess_game.chess_board.board[row][col]
                if piece:
                    piece_name = piece_map.get(str(piece), None)
                    if piece_name and piece_name in piece_images:
                        # Centering the pieces in the square
                        x = BOARD_X + col * CELL_SIZE + (CELL_SIZE - piece_images[piece_name].get_width()) // 2
                        y = BOARD_Y + row * CELL_SIZE + (CELL_SIZE - piece_images[piece_name].get_height()) // 2
                        screen.blit(piece_images[piece_name], (x, y))

    def draw_buttons(self, font):
        """Draw the control buttons."""
        button_x = BOARD_SIZE * CELL_SIZE + MARGIN + 20
        button_y = 50
        buttons = [
            ("New Game", self.new_game),
            ("Reset Game", self.reset_game),
            
            ("Solve by BFS",self.solve_by_bfs),
            ("Step by BFs", self.step_bfs),
            ("Solve by BrFS",self.solve_by_brfs),
            ("Step by BrFs", self.step_brfs),
        ]

        button_rects = []
        for text, _ in buttons:
            rect = pygame.Rect(button_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
            pygame.draw.rect(screen, ORANGE, rect)
            text_surface = font.render(text, True, BLACK)
            screen.blit(text_surface, (rect.centerx - text_surface.get_width() // 2,
                                       rect.centery - text_surface.get_height() // 2))
            button_rects.append(rect)
            button_y += BUTTON_HEIGHT + 10

        return button_rects, buttons

    def new_game(self):
        """Start a new game."""
        self.game = ChessGame()
        new_game_filename = generate_random_chess_input()
        self.load_game(new_game_filename)
                    
    def reset_game(self):
        """Reset the game to its initial state."""
        self.load_game(self.input)
        
            

    def solve_by_bfs(self):
        """Solve the game using DFS and display the solution."""
        #I want to invoke a animate function to animate the moves form the solution_moves list

        self.solution_moves, self.bfs_visited = best_first_search(self.game)
        if self.bfs_visited!= []: self.bfs_visited.pop(0)
        self.bfs = True
        
        if self.solution_moves == []:
            self.show_popup_message("No solution found.")
            return 
        self.animate_solution_moves() 

    def step_bfs(self):
        """Execute one step of DFS."""
        
        if not self.bfs:
            self.solution_moves, self.bfs_visited = best_first_search(self.game)
            if self.bfs_visited!= []: self.bfs_visited.pop(0)
            self.bfs = True
        
        if self.bfs_index < len(self.bfs_visited):
            
            self.game = self.bfs_visited[self.bfs_index]
            font = pygame.font.SysFont("Arial", 20)  # Ensure consistent font
            # print parent
            #if self.brfs_index:
            #    if self.brfs_visited[self.brfs_index-1] != self.game.parent:
            #        screen.fill(WHITE)
            #        self.draw_board()
            #        self.draw_pieces(self.game.parent)
            #        self.draw_buttons(font)
            #        pygame.display.flip()
            #        pygame.time.delay(750)
                    
            self.brfs_index +=1
            
            
            # print the next state
            screen.fill(WHITE)
            self.draw_board()
            self.draw_pieces(self.game)
            self.draw_buttons(font)
            pygame.display.flip()
            pygame.time.delay(500)
        else:
            self.show_popup_message("No more steps available.")

    def solve_by_brfs(self):
        """Solve the game using BFS and display the solution."""
        #I want to invoke a animate function to animate the moves form the solution_moves list
        
        
        self.solution_moves, self.brfs_visited = brfs(self.game)
        if self.brfs_visited!= []: self.brfs_visited.pop(0)
        self.brfs = True
        
        if self.solution_moves == []:
          
            self.show_popup_message("No solution found.")
            return 
        self.animate_solution_moves() 

    def step_brfs(self):
        """Execute one step of BFS."""
        if not self.brfs:
            self.solution_moves, self.brfs_visited = brfs(self.game)
            if self.brfs_visited!= []: self.brfs_visited.pop(0)
            self.brfs = True
        
        if self.brfs_index < len(self.brfs_visited):
            
            self.game = self.brfs_visited[self.brfs_index]
            font = pygame.font.SysFont("Arial", 20)  # Ensure consistent fon
            
            # print parent
            #if self.brfs_index:
            #    if self.brfs_visited[self.brfs_index-1] != self.game.parent:
            #        screen.fill(WHITE)
            #        self.draw_board()
            #        self.draw_pieces(self.game.parent)
            #        self.draw_buttons(font)
            #        pygame.display.flip()
            #        pygame.time.delay(750)
                    
            self.brfs_index +=1
            
            
            # print the next state
            screen.fill(WHITE)
            self.draw_board()
            self.draw_pieces(self.game)
            self.draw_buttons(font)
            pygame.display.flip()
            pygame.time.delay(500)
            
        else:
            self.show_popup_message("No more steps available.")

        
    def animate_solution_moves(self):
        """Animate the solution step by step."""
        for move in self.solution_moves:
            #print(move)
            start_square = move[:2]  # Example: "e2"
            end_square = move[2:]  # Example: "e4"

            start_col, start_row = self.game.chess_board.convert_valid_position(start_square)
            end_col, end_row = self.game.chess_board.convert_valid_position(end_square)
            
            # Move the piece on the board
            self.game.chess_board.update_board((start_col, start_row, end_col, end_row))

            # Redraw board and pieces to show animation
            screen.fill(WHITE)
            self.draw_board()
            self.draw_pieces(self.game)
            font = pygame.font.SysFont("Arial", 20)  # Ensure consistent font
            self.draw_buttons(font)
            pygame.display.flip()

            # Delay to make the animation visible
            pygame.time.delay(500)  # 500ms = 0.5 seconds
            
    def show_popup_message(self, message):
        """Display a pop-up message on the screen."""
        popup_width = 300
        popup_height = 100
        popup_x = (WINDOW_WIDTH - popup_width) // 2
        popup_y = (WINDOW_HEIGHT - popup_height) // 2

        popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)
        font = pygame.font.SysFont("Arial", 24, bold=True)

        screen.fill(WHITE)  # Redraw screen
        self.draw_board()
        self.draw_pieces(self.game)
        
        
        pygame.draw.rect(screen, ORANGE, popup_rect)  # Pop-up background
        text_surface = font.render(message, True, BLACK)
        text_rect = text_surface.get_rect(center=popup_rect.center)
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        pygame.time.delay(500)  # Show pop-up for 2 seconds
    
