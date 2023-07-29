import pygame.math

WIDTH = 300
HEIGHT = 800  # game height is 600 pixels

# setup option box
rect_width = 300
rect_height = 200
rect_x = 0
rect_y = 600

TILE_SIZE = 30  # each tile is 30 pixels long
# track position of individual tile and then crop image when player fills a row

vec_pos = pygame.math.Vector2  # creates a 2D vector commonly used to track the position of objects within pygame
# vector will look like (0, 0) simplifying position tracking

ANIMATION_DELAY = 150 # in milliseconds
BOARD_W = 10
BOARD_H = 20
BOARD_SIZE = BOARD_W, BOARD_H  # 200 tiles
BOARD_RES = BOARD_W * TILE_SIZE, BOARD_H * TILE_SIZE

START_POS_1 = vec_pos(BOARD_W // 2 - 1, 1)
NEXT_POS_OFFSET = vec_pos(BOARD_W * 0.6, BOARD_H * 1.2)
START_POS_2 = vec_pos(BOARD_W // 4 - 1, 0)
START_POS_3 = vec_pos(BOARD_W // 6 - 1, 0)
START_POSITIONS = [START_POS_1, START_POS_2, START_POS_3]
#print(START_POS)
DIRECTIONS = {
    "DOWN": vec_pos(0, 1),
    "RIGHT": vec_pos(1, 0),
    "LEFT": vec_pos(-1, 0)

}

VIS_COLS = 10
ROWS = 24
BOARD_COLOR = (48, 39, 32)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
KEYS = ["T", "O", "J", "L", "S", "I", "Z"]
SHAPE_COLORS = ["RedTile.png", "YellowTile.png", "GreenTile.png", "BlueTile.png"]
SHAPES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}

digits = pygame.image.load("Images/digits.png")

numbers = {
    0: digits.subsurface(pygame.Rect(0, 0, 21, 32)),
    1: digits.subsurface(pygame.Rect(21, 0, 21, 32)),
    2: digits.subsurface(pygame.Rect(42, 0, 21, 32)),
    3: digits.subsurface(pygame.Rect(63, 0, 21, 32)),
    4: digits.subsurface(pygame.Rect(84, 0, 21, 32)),
    5: digits.subsurface(pygame.Rect(105, 0, 21, 32)),
    6: digits.subsurface(pygame.Rect(126, 0, 21, 32)),
    7: digits.subsurface(pygame.Rect(147, 0, 21, 32)),
    8: digits.subsurface(pygame.Rect(168, 0, 21, 32)),
    9: digits.subsurface(pygame.Rect(189, 0, 21, 32))

}

