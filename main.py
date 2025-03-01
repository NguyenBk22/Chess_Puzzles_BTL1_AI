import pygame
from src.game import ChessGame
from src.utils import load_initial_position
from ChessUI import ChessPygame
from src.searching_algorithms.BrFS import brfs
from src.searching_algorithms.Best_First_Search import best_first_search

BOARD_SIZE = 8
CELL_SIZE = 80  # Each square size

WHITE = (255, 255, 255)

# Set up display
WINDOW_WIDTH = BOARD_SIZE * CELL_SIZE + 250
WINDOW_HEIGHT = BOARD_SIZE * CELL_SIZE + 50
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Chess Ranger")

def main():
    pygame.init()
    font = pygame.font.SysFont("Arial", 20)
    game = ChessPygame("data\\input1.txt")
    running = True

    while running:
        screen.fill(WHITE)
        game.draw_board()
        game.draw_pieces(game.game)
        button_rects, buttons = game.draw_buttons(font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for rect, action in zip(button_rects, buttons):
                    if rect.collidepoint(x, y):
                        action[1]()  # Call the associated function

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()