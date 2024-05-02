from time import perf_counter

import pygame.draw


class Particle():
    def __init__(self, pos, color, radius, lifetime):
        self.time = perf_counter()
        self.lifetime = lifetime
        self.radius = radius
        self.color = color
        self.pos = pos

        self.alive = True

    def draw(self, screen):
        if perf_counter() - self.time < self.lifetime:
            color = [i * (self.lifetime - perf_counter() + self.time) / self.lifetime for i in self.color]
            pygame.draw.circle(screen, color, self.pos, self.radius, 1)
        else:
            alive = False

    def update(self):
        pass