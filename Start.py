import pygame
from game import Game
import config

pygame.init()

# Create window
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

# Load textures
board_img = pygame.image.load("assets/board.png").convert_alpha()
board_img = pygame.transform.scale(board_img, (config.WIDTH, config.HEIGHT))
x_img = pygame.image.load("assets/x.png").convert_alpha()
o_img = pygame.image.load("assets/o.png").convert_alpha()

# Scale
x_img = pygame.transform.scale(x_img, (config.CELL_SIZE, config.CELL_SIZE))
o_img = pygame.transform.scale(o_img, (config.CELL_SIZE, config.CELL_SIZE))

# Game logic
game = Game()

def draw_board():
    """Draw the playing field and the X/O symbols."""
    screen.blit(board_img, (0, 0))

    for row in range(3):
        for col in range(3):
            value = game.board[row][col]
            pos = (col * config.CELL_SIZE, row * config.CELL_SIZE)
            if value == "X":
                screen.blit(x_img, pos)
            elif value == "O":
                screen.blit(o_img, pos)

def draw_winner():
    """Displays the winner or draw."""
    font = pygame.font.SysFont(None, 80)
    if game.winner:
        text = font.render(f"{game.winner} has won!", True, (255, 0, 0))
    elif game.is_draw():
        text = font.render("draw", True, (0, 0, 255))
    else:
        return
    # Show text in the middle
    screen.blit(text, (config.WIDTH // 2 - text.get_width() // 2,
                       config.HEIGHT // 2 - text.get_height() // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game.winner or game.is_draw():
                game.reset()
            else:
                x, y = pygame.mouse.get_pos()
                row = y // config.CELL_SIZE
                col = x // config.CELL_SIZE
                game.make_move(row, col)

    draw_board()
    draw_winner()

    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()