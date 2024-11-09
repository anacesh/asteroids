# pyright: basic
from circleshape import *
from constants import *
from shot import *
import random

class Asteroid(CircleShape):
    containers = []
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, player):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            player.score += 0.5
            player.radius += 0.1
            return

        player.score += 1
        # print(self.velocity, shot.velocity)
        angle = random.uniform(30,50)

        vec1 = self.velocity.rotate(angle)
        vec2 = self.velocity.rotate(-angle)
        # angto = self.velocity.angle_to(shot.velocity)
        # vec1 = self.velocity.rotate(angto + angle)
        # vec2 = self.velocity.rotate(angto - angle)
        rad = self.radius - ASTEROID_MIN_RADIUS


        ast1 = Asteroid(self.position.x, self.position.y, rad)
        ast2 = Asteroid(self.position.x, self.position.y, rad)
        ast1.velocity = vec1 * 1.2
        ast2.velocity = vec2 * 1.2

