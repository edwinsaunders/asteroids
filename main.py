import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Sprite groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add classes to groups for all instances
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (shots, updateable, drawable)

    # define all sprites after group definitions otherwise, NameError - group not defined
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    

    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("0x000000")

        for sprite in updateable:
            sprite.update(dt)

       
        
        # player collision check
        for sprite in asteroids:
            if player.collision_check(sprite):
                print("Game over!")
                return

        # shot collision check
        for ast_sprite in asteroids:
            for shot_sprite in shots:
                if ast_sprite.collision_check(shot_sprite):
                    #remove sprites from all groups
                    ast_sprite.kill()
                    shot_sprite.kill()


        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
    