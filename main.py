import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
            if asteroid.collides_with(player):
                print("Game is over")
                sys.exit()
        pygame.display.flip()
        
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
