import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # 1. Immediately kill the current asteroid
        self.kill()

        # 2. If it's a small asteroid, we are done
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # 3. Handle the splitting logic
        log_event("asteroid_split")

        # Pick a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the current one
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)

        # Calculate the new radius (original minus the minimum)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create the two smaller asteroids at the current position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1 * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2 * 1.2
