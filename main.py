# pyright: basic
import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = [updatable, drawable]
    Asteroid.containers = [asteroids, updatable, drawable]
    AsteroidField.containers = [updatable]
    Shot.containers = [shots, updatable, drawable]
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for obj in updatable:
            obj.update(dt)

        for ast in asteroids:
            for shot in shots:
                if ast.is_colliding(shot):
                    ast.split(shot)
                    shot.kill()


            if ast.is_colliding(player):
                exit("Game over!")

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        pygame.display.set_caption(f"Asteroids, Frametime: {dt}")


if __name__ == "__main__":
    main()
