import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    cluck = pygame.time.Clock()
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    dt = 0
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # pygame.Surface.fill(screen, (0, 0, 0))
        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = cluck.tick(60)/1000

if __name__ == '__main__':
    main()