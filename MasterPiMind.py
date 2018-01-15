#! /usr/bin/python3

from enum import Enum
import pygame
from pygame.locals import *
from pygame import gfxdraw


class GameColor(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (244, 67, 54)
    PINK = (244, 67, 54)
    PURPLE = (156, 39, 176)
    BLUE = (33, 150, 243)
    GREEN = (76, 175, 80)
    YELLOW = (255, 235, 59)
    ORANGE = (255, 152, 0)
    BROWN = (121, 85, 72)
    BROWN_DARK = (62, 39, 35)


def AAfilledRoundedRect(surface, rect, color, radius=0.4):
    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect = Rect(rect)
    color = Color(*color)
    alpha = color.a
    color.a = 0
    pos = rect.topleft
    rect.topleft = 0, 0
    rectangle = pygame.Surface(rect.size, SRCALPHA)

    circle = pygame.Surface([min(rect.size) * 3] * 2, SRCALPHA)
    pygame.draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
    circle = pygame.transform.smoothscale(circle, [int(min(rect.size) * radius)] * 2)

    radius = rectangle.blit(circle, (0, 0))
    radius.bottomright = rect.bottomright
    rectangle.blit(circle, radius)
    radius.topright = rect.topright
    rectangle.blit(circle, radius)
    radius.bottomleft = rect.bottomleft
    rectangle.blit(circle, radius)

    rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
    rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))

    rectangle.fill(color, special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255, 255, 255, alpha), special_flags=BLEND_RGBA_MIN)

    return surface.blit(rectangle, pos)

pygame.init()

window = pygame.display.set_mode((1000, 900))

running = 1

window.fill(GameColor.WHITE.value)

AAfilledRoundedRect(window, (250, 25, 500, 850), GameColor.BROWN.value, 0.1)

for i in range(130, 850, 80):
    pygame.draw.line(window, GameColor.BROWN_DARK.value, (270, i), (730, i), 2)

for l in range(90, 890, 80):
    for r in range(380, 660, 80):
        pygame.gfxdraw.aacircle(window, r, l, 15, GameColor.BROWN_DARK.value)
        pygame.gfxdraw.filled_circle(window, r, l, 15, GameColor.BROWN_DARK.value)
        pygame.gfxdraw.aacircle(window, r, l, 20, GameColor.BROWN_DARK.value)

i = 100
for color in GameColor:
    pygame.gfxdraw.aacircle(window, 50, i, 20, color.value)
    pygame.gfxdraw.filled_circle(window, 50, i, 20, color.value)
    i += 50

pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
