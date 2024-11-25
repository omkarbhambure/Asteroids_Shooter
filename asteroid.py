from circleshape import CircleShape
import pygame
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, radius = self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)
        v1_radius = self.radius - ASTEROID_MIN_RADIUS
        v2_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, v1_radius)
        ast1.velocity = v1*1.2
        ast2 = Asteroid(self.position.x, self.position.y, v2_radius)
        ast2.velocity = v2*1.2
        



