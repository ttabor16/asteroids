import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle_change = random.uniform(20, 50)
            new_angle1 = self.velocity.rotate(angle_change)
            new_angle2 = self.velocity.rotate(-angle_change)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position[0],self.position[1], new_radius)
            asteroid1.velocity = new_angle1 * 1.2
            asteroid2 = Asteroid(self.position[0],self.position[1], new_radius)
            asteroid2.velocity = new_angle2 * 1.2

    