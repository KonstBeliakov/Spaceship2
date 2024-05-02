from time import perf_counter
import pygame
from utils import *


def line(color, x1, y1, x2, y2, player_pos, screen_size, screen):
    pygame.draw.line(screen, color, [x1, y1], [x2, y2])#[x1 - player_pos[0] + screen_size[0] // 2, y1 - player_pos[1] + screen_size[0] // 2],
                     #[x2 - player_pos[0] + screen_size[0] // 2, y2 - player_pos[1] + screen_size[0] // 2])


class Object():
    def __init__(self):
        self.hp = 100
        self.sizeX = 32
        self.sizeY = 32
        self.x = 0
        self.y = 0
        self.speedX = 0
        self.speedY = 0
        self.direction = 0
        self.time = perf_counter()
        self.image = None

        self.selected = False

        self.push_off_edge = True

        self.hitbox = True

    def update(self, player_pos, screen_size, screen):
        if self.hp > 0:
            old_pos = self.pos()

            self.x += self.speedX * (perf_counter() - self.time)
            self.y += self.speedY * (perf_counter() - self.time)
            self.time = perf_counter()

            if self.push_off_edge:
                if self.x - player_pos[0] < 0 or self.x - player_pos[0] > screen_size[0]:
                    self.speedX *= -1
                if self.y - player_pos[1] < 0 or self.y - player_pos[1] > screen_size[1]:
                    self.speedY *= -1

            angles = [self.pos(),
                      (self.x + self.sizeX, self.y),
                      (self.x + self.sizeX, self.y + self.sizeY),
                      (self.x, self.y + self.sizeY)]
            segments = [[angles[j], angles[(j + 1) % 4]] for j in range(4)]
            pygame.draw.line(screen, (0, 255, 0), old_pos, self.pos())
            if self.hitbox:
                for segment in segments:
                    pygame.draw.line(screen, (255 - int(self.hp * 255 / 100), int(self.hp * 255 / 100), 0), segment[0], segment[1])
            pygame.draw.line(screen, (0, 255, 0), old_pos, self.pos())

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_speed(self, speedX, speedY):
        self.speedX = speedX
        self.speedY = speedY

    def pos(self):
        return [self.x, self.y]

    def get_size(self):
        return [self.sizeX, self.sizeY]

    def draw(self, screen, player_pos):
        pass
        '''if self.image is None:
            self.image = pygame.image.load('default.png').convert_alpha()
        if self.image.get_size()[0] != self.sizeX or self.image.get_size()[1] != self.sizeY:
            self.image = pygame.transform.scale(self.image, (self.sizeX, self.sizeY))
        if self.selected:
            pygame.draw.rect(screen, (0, 255, 0), (self.x - player_pos[0] - self.sizeX // 2 - 4,
                                                   self.y - player_pos[1] - self.sizeY // 2 - 4, self.sizeX + 8,
                                                   self.sizeY + 8), 2)
        img_rotated, img_rotated_rect = rotate(self.image, self.direction,
                                               (self.x - player_pos[0], self.y - player_pos[1]))
        screen.blit(img_rotated, img_rotated_rect)'''
