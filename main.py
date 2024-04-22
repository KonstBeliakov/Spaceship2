import pygame as pg
from random import randint
from turret import Turret
from object import Object
from bullet import Bullet

pg.init()
window_size = (1200, 800)
screen_center = (-600, -400)
pg.display.set_caption("Window")
screen = pg.display.set_mode(window_size)
background_color = (0, 0, 0)

turret = Turret()

objects = [Object() for i in range(10)]
for object in objects:
    object.set_position(randint(-500, 500), randint(-500, 500))
    object.set_speed(randint(-10, 10), randint(-10, 10))

bullets = []

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.fill(background_color)

    turret.update(screen_center, window_size, objects, bullets)
    turret.draw(screen, screen_center)

    for obj in objects:
        obj.update(screen_center, window_size)
        obj.draw(screen, screen_center)

    for i in range(len(objects) - 1, -1, -1):
        if objects[i].hp < 0:
            del objects[i]

    for i in range(len(bullets)):
        bullets[i].update(screen_center, window_size, objects)
        bullets[i].draw(screen, screen_center)

    for i in range(len(bullets) - 1, -1, -1):
        if bullets[i].hp < 0:
            del bullets[i]

    pg.display.flip()