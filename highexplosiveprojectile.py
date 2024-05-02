from projectile import Projectile
from particle import Particle
from utils import *


class HighExplosiveProjectile(Projectile):
    def __init__(self, pos, speed):
        super().__init__(pos, speed)
        self.radius = 150
        self.damage = 50

    def explode(self, objects, index, particles):
        particles.append(Particle(self.pos(), (255, 100, 0), self.radius, 1))
        for object in objects:
            if dist(object.pos(), objects[index].pos()) < self.radius:
                object.hp -= self.damage * (self.radius - dist(object.pos(), objects[index].pos())) / self.radius

