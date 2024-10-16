import pygame

from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Sprite groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)

    # define all sprites after group definitions otherwise, NameError - group not defined
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    

    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("0x000000")
        for sprite in updateable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
    