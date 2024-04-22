import pygame as pg


def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5


def dist(pos1, pos2):
    return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** .5


def point_in_square(point_pos, square_pos, square_size):
    return square_pos[0] + square_size[0] >= point_pos[0] >= square_pos[0] and\
        square_pos[1] + square_size[1] >= point_pos[1] >= square_pos[1]


def itersection_of_segments(a1, a2, b1, b2):
    a1, a2 = min(a1, a2), max(a1, a2)
    b1, b2 = min(b1, b2), max(b1, b2)

    return a1 <= b1 <= a2 or a1 <= b2 <= a2 or b1 <= a1 <= b2 or b1 <= a2 <= b2


def squares_intersection(pos1, size1, pos2, size2):
    return itersection_of_segments(pos1[0], pos1[0] + size1[0], pos2[0], pos2[0] + size2[0]) and\
        itersection_of_segments(pos1[1], pos1[1] + size1[1], pos2[1], pos2[1] + size2[1])


def sign(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    return 1


def rotate(surface, angle, position):
    img = pg.transform.rotozoom(surface, angle, 1)
    img_rect = img.get_rect(center=position)
    return img, img_rect


if __name__ == '__main__':
    pos1 = [int(i) for i in input().split()]
    size1 = [int(i) for i in input().split()]
    pos2 = [int(i) for i in input().split()]
    size2 = [int(i) for i in input().split()]
    print(squares_intersection(pos1, size1, pos2, size2))