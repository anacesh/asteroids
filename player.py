# pyright: basic
import pygame

from Assets.assets import Assets
from circleshape import *
from constants import *
from shot import *
import shot
import time


class Player(CircleShape):
    containers = []
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.fire_rate = 0
        self.score = 0
        self.lives = PLAYER_LIVES
        self.iframes = 0 # какой еще ифрейм?)


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        mousepos = self.position - pygame.mouse.get_pos()
        mousevec = pygame.Vector2(mousepos)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        angto = forward.angle_to(mousevec)
        self.rotation += (angto + 180) 
        self.rotation = self.rotation % 360

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        self.fire_rate -= 1 * dt
        self.iframes -= 1
        keys = pygame.key.get_pressed()
        self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(dt * -1)

        if keys[pygame.K_SPACE]:
            self.shoot()


    def shoot(self):
        if self.fire_rate <= 0:
            shot = Shot(self.position.x, self.position.y)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = forward
            self.fire_rate = PLAYER_FIRE_COOLDOWN
            Assets.get_instance().audio.play_shot_sound()
            # all_sounds.get("shot1", None).play()

    def die(self):
        if self.iframes <= 0:
            if self.lives == 0:
                # all_sounds.get("we_lost", None).play()
                Assets.get_instance().audio.sounds.get("we_lost").play()
                time.sleep(1)
                exit("Game Over!")
            Assets.get_instance().audio.sounds.get("hero_damage").play()
            self.lives -= 1
            # all_sounds.get("hero_damage", None).play()
            self.iframes = PLAYER_IFRAMES
            self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


