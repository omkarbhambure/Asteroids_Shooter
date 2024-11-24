import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    cluck = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    dt = 0
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # pygame.Surface.fill(screen, (0, 0, 0))
        for ob in updatable:
            ob.update(dt)
        #player.update(dt)
        screen.fill("black")
        for ob in drawable:
            ob.draw(screen)
        #player.draw(screen)
        pygame.display.flip()
        dt = cluck.tick(60)/1000

if __name__ == '__main__':
    main()