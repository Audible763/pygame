# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    #all objects that can be updated
    updatable = pygame.sprite.Group()

    #all objects that can be drawn
    drawable = pygame.sprite.Group()

    #all asteroid objects
    asteroids = pygame.sprite.Group()

    #adds all instances of Player to upd and draw Groups
    Player.containers = (updatable, drawable)

    #adds all instances of Asteroid to asteroids, upd, and draw Groups
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        screen.fill(color="black")
        for draw_obj in drawable:
            draw_obj.draw(screen)
        pygame.display.flip()

        dt = timer.tick(60) / 1000


if __name__ == "__main__":
    main()