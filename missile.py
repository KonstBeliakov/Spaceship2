from highexplosiveprojectile import HighExplosiveProjectile
from time import perf_counter
import math
from utils import *


class Missile(HighExplosiveProjectile):
    def __init__(self, pos, speed):
        super().__init__(pos, speed)
        self.turning_counter = perf_counter()
        self.rotation_speed = 1

    def update(self, player_pos, screen_size, objects, screen, particles):
        super().update(player_pos, screen_size, objects, screen, particles)

        target = min(objects, key=lambda obj: dist(obj.pos(), self.pos()))

        dx = (target.x + target.get_size()[0] // 2 - self.x)
        dy = (target.y + target.get_size()[0] // 2 - self.y)
        vx = self.speedX
        vy = self.speedY

        alpha = math.atan2(vx, vy)
        target_alpha = math.atan2(dx, dy)

        if 0 < (alpha - target_alpha) < math.pi:
            alpha -= self.rotation_speed * (perf_counter() - self.turning_counter)
        else:
            alpha += self.rotation_speed * (perf_counter() - self.turning_counter)

        speed = (self.speedX ** 2 + self.speedY ** 2) ** .5
        self.speedX = speed * math.sin(alpha)
        self.speedY = speed * math.cos(alpha)

        self.turning_counter = perf_counter()
