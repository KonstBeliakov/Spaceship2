import pygame as pg
from random import randint
from object import Object
from spaceship import Spaceship
from highexplosiveprojectile import HighExplosiveProjectile

pg.init()
window_size = (1200, 800)
screen_center = (0, 0) #  (600, 400)
pg.display.set_caption("Window")
screen = pg.display.set_mode(window_size)
background_color = (0, 0, 0)

spaceship = Spaceship()

objects = [Object() for i in range(50)]
for object in objects:
    object.set_position(randint(0, 1000), randint(0, 1000))
    object.set_speed(randint(-10, 10), randint(-10, 10))

bullets = []
particles = []

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        spaceship.interaction_with_player(event, screen_center)

    screen.fill(background_color)

    spaceship.update(screen_center, window_size, objects, bullets, screen)
    spaceship.draw(screen, screen_center)

    for particle in particles:
        particle.update()
        particle.draw(screen)

    for obj in objects:
        obj.update(screen_center, window_size, screen)
        #obj.draw(screen, screen_center)

    for i in range(len(objects) - 1, -1, -1):
        if objects[i].hp < 0:
            del objects[i]

    for i in range(len(bullets)):
        #bullets[i].draw(screen, screen_center)
        bullets[i].update(screen_center, window_size, objects, screen, particles)

    for i in range(len(bullets) - 1, -1, -1):
        if bullets[i].hp < 0:
            del bullets[i]

    pg.display.flip()