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
    font = pygame.font.Font("inter.ttf", 24)
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
        text_surface = font.render(f"Score: {player.score}", True, (255, 255, 255))
        screen.blit(text_surface, (SCREEN_WIDTH - 200, 20))

        for obj in drawable:
            obj.draw(screen)

        for obj in updatable:
            obj.update(dt)

        for ast in asteroids:
            for shot in shots:
                if ast.is_colliding(shot):
                    ast.split(player)
                    shot.kill()


            if ast.is_colliding(player):
                exit("Game over!")

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        pygame.display.set_caption(f"Asteroids, Score: {player.score}")


if __name__ == "__main__":
    main()
