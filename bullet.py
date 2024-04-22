from object import Object
from utils import *


class Bullet(Object):
    def __init__(self, pos, speed):
        super().__init__()
        self.speedX = speed[0]
        self.speedY = speed[1]

        self.x = pos[0]
        self.y = pos[1]

        self.sizeX = 8
        self.sizeY = 8

        self.push_off_edge = False

    def update(self, player_pos, screen_size, objects):
        super().update(player_pos, screen_size)

        if self.x - player_pos[0] < 0 or self.x - player_pos[0] > screen_size[0] or \
                self.y - player_pos[1] < 0 or self.y - player_pos[1] > screen_size[1]:
            self.hp = -1

        for i in range(len(objects)):
            if squares_intersection(self.pos(), self.get_size(), objects[i].pos(), objects[i].get_size()):
                objects[i].hp -= 101
                self.hp = -1
                break
