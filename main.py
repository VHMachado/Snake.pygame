import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0)
    
    def draw_snake(self):
        for block in self.body:
            x = int(block.x * cell_size)
            y = int(block.y * cell_size)
            w = h = cell_size
            snake_rect_size = (x, y, w, h)
            snake_rect = pygame.Rect(snake_rect_size)
            pygame.draw.rect(screen, (183,111,122), snake_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        x = int(self.pos.x * cell_size)
        y = int(self.pos.y * cell_size)
        w = h = cell_size
        fruit_rect_size = (x, y, w, h)
        fruit_rect = pygame.Rect(fruit_rect_size)
        pygame.draw.rect(screen, (126,166,114), fruit_rect)

pygame.init()

cell_size = 30
cell_number = 20
dimensions = cell_number * cell_size

screen_size = (width, height) = dimensions, dimensions
screen = pygame.display.set_mode((screen_size))

fruit = FRUIT()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

clock = pygame.time.Clock()
framerate = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1,0)
                
    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(framerate)