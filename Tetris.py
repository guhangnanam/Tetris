from Constants import *
import math
import pygame
from Tetrimino import *



# Tetris class
# The Tetris class contains a Tetrimino object as an attribute
# Important to understand: Sprites in python are a separate class included in the Pygame package. Sprites combine the surface and rect functions of images into one class for simplicity.
# To move or manipulate an image on pygame an image must first be given a "rect" which can then be moved with the image. Surfaces themselves cannot be moved.
# Sprites can be added to sprite groups to simplify the display process. Sprites cannot be displayed outside of groups
# Sprite groups can be updated by themselves which helps us to create moving objects. This is also why each class has an update method


class Tetris:

    def __init__(self, screen):
        self.screen = screen
        self.sprite_group = pygame.sprite.Group()
        self.tetrimino = Tetrimino(self)
        self.next_tetrimino = Tetrimino(self, current=False)

        self.last_fall = pygame.time.get_ticks()  # time of last automatic fall of tetrimino
        self.field = self.create_field()

        self.restart_button = pygame.image.load("Images/restart.png")
        self.restart_rect = self.restart_button.get_rect()
        self.restart_rect.topleft = (20, 700)

        self.text = pygame.image.load("Images/Next.png")
        self.text_rect = self.text.get_rect()
        self.text_rect.topleft = (150, 600)

        self.score = 0
        self.digit1 = numbers[0]
        self.digit1_rect = self.digit1.get_rect()
        self.digit1_rect.topleft = (10, 625)

        self.digit2 = numbers[0]
        self.digit2_rect = self.digit2.get_rect()
        self.digit2_rect.topleft = (31, 625)

        self.digit3 = numbers[0]
        self.digit3_rect = self.digit3.get_rect()
        self.digit3_rect.topleft = (52, 625)

        self.digit4 = numbers[0]
        self.digit4_rect = self.digit4.get_rect()
        self.digit4_rect.topleft = (73, 625 )


    def is_game_over(self):

        if self.tetrimino.tiles[0].position.y == START_POS_1[1]: # check the tetriminos y position to see if it is the same as the start position to determine if it has moved or not
            pygame.time.wait(300)       # if it hasn't moved from the start position than the player has lost
            return True



    def check_full_lines(self):

        row = BOARD_H - 1
        for y in range(BOARD_H - 1, -1, -1): # start at 19 and iterate until -1 by decrementing by 1
            for x in range(BOARD_W):
                self.field[row][x] = self.field[y][x]

                if self.field[y][x]:
                    self.field[row][x].position = vec_pos(x, y)

            if sum(map(bool, self.field[y])) < BOARD_W:
                row -= 1
            else:
                self.score += 100
                self.check_score()
                #print(self.score)
                for x in range(BOARD_W):            # for the entire width of the row
                    self.field[row][x].inplay = False       # take the tile out of play
                    self.field[row][x] = 0              # set the field spot to be 0 (so there is no tile there)



    def place_tetrimino_field(self):
        for tile in self.tetrimino.tiles:
            x, y = int(tile.position.x), int(tile.position.y) # use the int function because tile position is stored as 2D pygame vector

            if (y >= 0 and y < BOARD_H and x >= 0 and x < BOARD_W): # only place the on the field if it is within the confines of the board, this prevents tetriminos from colliding when the spawn
                self.field[y][x] = tile   # place tile within the field

            #print(self.field[y][x])

    def create_field(self):
        # This function will create a 2D array that is the same height and width as the game
        # This will allow us to track which squares are occupied by Tetriminos and therefore must have collision physics
        field = [[0 for x in range(BOARD_W)] for y in range(BOARD_H)]

        return field


    def draw_grid(self):
        for i in range(BOARD_W):
            for j in range(BOARD_H):
                pygame.draw.rect(self.screen, BLACK,( i * TILE_SIZE, j * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def draw_box(self):
        pygame.draw.rect(self.screen, WHITE, (rect_x, rect_y, rect_width, rect_height))

    def draw_restart_button(self):
        self.screen.blit(self.restart_button, self.restart_rect)

    def check_restart(self, x, y):
        if self.restart_rect.collidepoint(x, y):
            self.__init__(self.screen)

    def draw_next(self):
        self.screen.blit(self.text, self.text_rect)

    def check_score(self):
        if self.score < 1000:
            first_digit = 0
            second_digit = self.score // 100
            third_digit = (self.score % 100) // 10
            fourth_digit = self.score % 10

        elif self.score >= 1000:
            first_digit = self.score // 1000  # Get the first digit (thousands place)
            second_digit = (self.score % 1000) // 100  # Get the second digit (hundreds place)
            third_digit = (self.score % 100) // 10  # Get the third digit (tens place)
            fourth_digit = self.score % 10  # Get the fourth digit (ones place)
        else:
            first_digit = 0
            second_digit = 0
            third_digit = 0
            fourth_digit = 0

        self.digit1 = numbers[first_digit]
        self.digit2 = numbers[second_digit]
        self.digit3 = numbers[third_digit]
        self.digit4 = numbers[fourth_digit]

    def draw_scoreboard(self):
        self.screen.blit(self.digit1, self.digit1_rect)
        self.screen.blit(self.digit2, self.digit2_rect)
        self.screen.blit(self.digit3, self.digit3_rect)
        self.screen.blit(self.digit4, self.digit4_rect)


    def move(self, key):   # move tetrimino according to key pushes
        if key == pygame.K_LEFT:
            self.tetrimino.move("LEFT")
        if key == pygame.K_RIGHT:
            self.tetrimino.move("RIGHT")
        if key == pygame.K_DOWN:
            self.tetrimino.move("DOWN")

    def rotate(self, key):
        if key == pygame.K_UP:
            self.tetrimino.rotate()

    def check_placed(self):
        if self.tetrimino.placed:
            if self.is_game_over():
                self.__init__(self.screen)
            else:
                self.place_tetrimino_field() # call this to place tetrimino on field before tetrimino is updated
                self.next_tetrimino.current = True
                self.tetrimino = self.next_tetrimino # create a new tetrimino if tetrimino has been placed
                self.next_tetrimino = Tetrimino(self, current=False)

    def update(self):

        current_time = pygame.time.get_ticks()   # current time at update
        time_elapsed = current_time - self.last_fall        # time since last fall

        if time_elapsed >= 1000 // 1:   # if a second has passed then update the tetrimino's position
            self.tetrimino.update()
            self.last_fall = current_time # set last fall time to be equal to current time


        self.check_placed()
        self.check_full_lines()
        self.sprite_group.update()

    def draw(self):
        self.check_placed()
        self.draw_grid()
        self.draw_box()
        self.draw_restart_button()
        self.draw_next()
        self.draw_scoreboard()
        for tile in self.tetrimino.tiles:
            tile.set_rect_pos()

        self.sprite_group.draw(self.screen)
        pygame.display.update()


