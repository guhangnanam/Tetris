import pygame
from Constants import *
from Tetris import *

# Basic structure inspired by Coder Space video https://www.youtube.com/watch?v=RxWS5h1UfI4
# all original code

# Development is broken into layers
# Outermost: Game Layer
# Tetris layer
# Tetrimino layer
# Tile layer

# This is the Game Layer where the code is called upon and run from the other classes
# Surfaces are just things that can be drawn onto the screen for the user to see. There is  obviously the base background surface but also additional surfaces can be created.

def main():
    pygame.init()

    # setup game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BOARD_COLOR)
    pygame.display.set_caption("Tetris")
    pygame.display.update()
    clock = pygame.time.Clock() # Will be later used to set the frame rate of the game

    tetris = Tetris(screen)


    running = True
    while running:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    tetris.check_restart(mouse_x, mouse_y)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                tetris.move(pygame.K_DOWN)
            elif keys[pygame.K_LEFT]:
                tetris.move(pygame.K_LEFT)
            elif keys[pygame.K_RIGHT]:
                tetris.move(pygame.K_RIGHT)
            elif keys[pygame.K_UP]:
                tetris.rotate(pygame.K_UP)


        screen.fill(BOARD_COLOR)
        tetris.update()
        tetris.draw()
        pygame.display.flip()
        pygame.display.update()

        #clock.tick(8)


    pygame.quit()















if __name__ == "__main__":
    main()
