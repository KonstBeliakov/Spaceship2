import pygame
from object import Object
from turret import *
from utils import *


class Spaceship(Object):
    def __init__(self):
        self.grid_sizeX, self.grid_sizeY = 5, 7
        self.detail = [[None] * self.grid_sizeY for _ in range(self.grid_sizeX)]
        self.detail[0][0] = Turret()
        self.detail_size = 32

    def interaction_with_player(self, event, player_pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = (event.pos[0] + player_pos[0]) // self.detail_size
            y = (event.pos[1] + player_pos[1]) // self.detail_size
            if 0 <= x < self.grid_sizeX and 0 <= y < self.grid_sizeY:
                self.detail[x][y] = Turret()
                self.detail[x][y].set_position(x * self.detail_size, y * self.detail_size)
            print('click')

    def update(self, player_pos, screen_size, enemies, bullets, screen):
        for i in range(self.grid_sizeX):
            for j in range(self.grid_sizeY):
                if self.detail[i][j] is not None:
                    if isinstance(self.detail[i][j], Turret):
                        self.detail[i][j].update(player_pos, screen_size, enemies, bullets, screen)
                    else:
                        self.detail[i][j].update(player_pos, screen_size, screen)

    def draw(self, screen, player_pos):
        for i in range(self.grid_sizeX):
            for j in range(self.grid_sizeY):
                if self.detail[i][j] is not None:
                    self.detail[i][j].draw(screen, player_pos)

