# pyright: basic
from circleshape import *
from constants import *

class Shot(CircleShape):
    containers = []
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1)

    def draw(self, screen):
        pygame.draw.circle(screen, "orange", self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * PLAYER_SHOOT_SPEED * dt
