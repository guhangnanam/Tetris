import random

from Constants import *
from Tetris import *
import pygame
import math

class Tile(pygame.sprite.Sprite):

    def __init__(self, color, tetrimino, position):
        self.tetrimino = tetrimino  # tetrimino object inherit from higher class
        self.color = color
        self.position = vec_pos(position) + START_POS_1
        self.next_position = vec_pos(position) + NEXT_POS_OFFSET
        self.inplay = True

        super().__init__(tetrimino.tetris.sprite_group)
        self.image = pygame.image.load("Images/" + self.color)
        #self.image.blit(self.tile, self.rect)
        #self.image = pygame.Surface([TILE_SIZE, TILE_SIZE])
        #self.image.fill("orange")
        self.rect = self.image.get_rect()
        #self.rect.topleft = self.position * TILE_SIZE

        # string = "Images/" + self.color
        # print(string)

        self.tile = pygame.image.load("Images/" + self.color)
        self.image.blit(self.tile, self.rect)


    def check_inplay(self):
        if not self.inplay:
            self.kill()

    def set_rect_pos(self):
        pos = [self.next_position, self.position][self.tetrimino.current]
        self.rect.topleft = pos * TILE_SIZE

    def update(self):
        self.check_inplay()
        self.set_rect_pos()

    def rotate(self, pivot):
        # rotation process occurs in 3 steps
        # 1. Subtract pivot from current position
        # 2. Rotate the resulting position 90 degrees
        # 3. Add the pivot back into the current
        #print(pivot)
        #print(self.position)
        curr_minus_pivot = self.position - pivot
        #print(curr_minus_pivot)
        rotated = curr_minus_pivot.rotate(90)   # another benefit of using the 2D vector built into pygame (allows me to use built in function to rotate coordinates)
        #print(rotated)
        final_plus_pivot = rotated + pivot
        #print(final_plus_pivot)

        return final_plus_pivot


    def collision(self, position):
        x_pos, y_pos = int(position.x), int(position.y)
        # check if it is within the confines of the board
        if (0 <= x_pos < BOARD_W and 0 <= y_pos < BOARD_H and (y_pos <= 0 or not self.tetrimino.tetris.field[y_pos][x_pos])):

            return False
        else:
            return True






class Tetrimino:

    def __init__(self, tetris, current=True):
        self.tetris = tetris     # inherit a tetris object from Tetris class
        rand_color = random.choice(SHAPE_COLORS)        # generate a random color from a list of existing colors (red, yellow, blue, green)
        self.type = random.choice(KEYS)         # store the type of the shape
        #self.type = KEYS[5]
        self.tiles = [Tile(rand_color, self, pos) for pos in SHAPES[self.type]]   # create a list of Tile objects that will form the Tetrimino
        self.placed = False # Has the tetrimino been placed at the bottom
        self.current = current


    def check_collision(self, potential_positions):
        valid = map(Tile.collision, self.tiles, potential_positions)
        #print(valid)

        if True in valid:   # if there is an instance where a tile collides with a wall return true
            return True
        else:
            return False        # otherwise return false

    def rotate(self): # NOT CURRENTLY WORKING
        #pivot_pos = self.tiles[0].position # pivot will always be the block with the index position of 0 (first coordinate)
        #print(pivot_pos)
        pivot_tile = self.tiles[-1]
        pivot = pivot_tile.position

        # Now similar to what we did in the move function we must check the potential position of the rotation and see if it causes a collision
        # if it doesn't then we can proceed to rotate the tetrimino

        potential_rotate_pos = [tile.rotate(pivot) for tile in self.tiles]

        if not self.check_collision(potential_rotate_pos):
            for i, tile in enumerate(self.tiles[:-1]):
                tile.position = potential_rotate_pos[i]    # assign positions to potential positions if they check out


    def move(self, direction):
        distance = DIRECTIONS[direction] # pull correct direction from dictionary
        #print(distance)

        potential_pos = [tile.position + distance for tile in self.tiles]       # create a list of the potential position if tetrimino is moved
        collision = self.check_collision(potential_pos)                         # check to see if any of those positions cause collisions


        if not collision:       # if not in collision with wall move tetrimino
            for tile in self.tiles:
                #print(self.tiles)

                tile.position += distance                 # adjust position accordingly

        elif direction == "DOWN": #and collision:   # as soon as a collision occurs and the direction is down
            self.placed = True

    def update(self):
        #self.rotate()
        self.move(direction="DOWN")
