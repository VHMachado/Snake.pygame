import pygame, sys
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = 5
        self.y = 4
        self.pos = Vector2(self.x, self.y)
    def draw_fruit(self):
        fruit_rect_size = (x, y, w, h) = self.pos.x, self.pos.y, cell_size, cell_size
        fruit_rect = pygame.Rect(fruit_rect_size)
        pygame.draw.rect(screen, (126,166,114), fruit_rect)

pygame.init()

cell_size = 30
cell_number = 20
dimensions = cell_number * cell_size

screen_size = (width, height) = dimensions, dimensions
screen = pygame.display.set_mode((screen_size))

# rect_size_draw = x, y, w, h = 100, 200, 50, 50
# test_rect_draw = pygame.Rect(rect_size)

# surface_size = (width, height) = 100, 200
# test_surface = pygame.Surface((surface_size))
# test_rect = test_surface.get_rect(center = (200,250))
# test_surface.fill('light blue')

fruit = FRUIT()

screen.fill((175,215,70))

clock = pygame.time.Clock()
framerate = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # pygame.draw.ellipse(screen, pygame.Color('red'), test_rect_draw)
    # screen.blit(test_surface,test_rect)
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(framerate)