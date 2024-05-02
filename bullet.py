import pygame

import utils
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
        self.hitbox = False

    def update(self, player_pos, screen_size, objects, screen):
        old_pos = self.pos()

        super().update(player_pos, screen_size, screen)

        if self.x - player_pos[0] < 0 or self.x - player_pos[0] > screen_size[0] or \
                self.y - player_pos[1] < 0 or self.y - player_pos[1] > screen_size[1]:
            self.hp = -1

        for i in range(len(objects)):
            obj = objects[i]
            object_angles = [obj.pos(),
                             (obj.x + obj.sizeX, obj.y),
                             (obj.x + obj.sizeX, obj.y + obj.sizeY),
                             (obj.x, obj.y + obj.sizeY)]
            segments = [[object_angles[j], object_angles[(j + 1) % 4]] for j in range(4)]
            shooting_segment = utils.Segment(old_pos, self.pos())
            if any([line_segments_intersection(shooting_segment, Segment(*segments[j])) for j in range(4)]):
                objects[i].hp -= 5
                self.hp = -1
                break
