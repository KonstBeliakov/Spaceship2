import pygame

from bullet import Bullet
from object import Object
from utils import *
from time import perf_counter


class Turret(Object):
    def __init__(self):
        super().__init__()
        self.range = 10000
        self.direction = 0
        self.angle = 360
        self.bullet_speed = 100
        self.frequency = 2

        self.shoot_time = perf_counter()

        self.image = pygame.image.load('turret.png').convert_alpha()

    def update(self, player_pos, screen_size, enemies, bullets):
        super().update(player_pos, screen_size)
        self.shoot(enemies, bullets)

    def shoot(self, enemies, bullets):
        if perf_counter() - self.shoot_time > (1 / self.frequency):
            for enemy in enemies:
                enemy.selected = False
            enemy = min(enemies, key=lambda enemy: dist(enemy.pos(), self.pos()))
            enemy.selected = True
            if dist(enemy.pos(), self.pos()) <= self.range:
                self.shoot_time += 1 / self.frequency

                dx = enemy.x - self.x
                dy = enemy.y - self.y
                speedX = self.bullet_speed / ((1 + (dy ** 2 / dx ** 2)) ** 0.5)
                speedY = speedX * dy / dx
                bullets.append(Bullet(self.pos(), [speedX * sign(dx), speedY * sign(dx)]))
