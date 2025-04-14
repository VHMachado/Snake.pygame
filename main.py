import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.grow_snake = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()

    def draw_snake(self):
        for block in self.body:
            x = int(block.x * cell_size)
            y = int(block.y * cell_size)
            w = h = cell_size
            snake_rect_size = (x, y, w, h)
            snake_rect = pygame.Rect(snake_rect_size)
            pygame.draw.rect(screen, (183,111,122), snake_rect)

    def move_snake(self):
        if self.grow_snake == True:
            body_copy = self.body[:]
            self.grow_snake = False
        else: 
            body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        self.grow_snake = True

class FRUIT:
    def __init__(self):
        self.randomize_position()
        self.apple = pygame.image.load('Graphics/apple.png').convert_alpha()

    def draw_fruit(self):
        x = int(self.pos.x * cell_size)
        y = int(self.pos.y * cell_size)
        w = h = cell_size
        fruit_rect_size = (x, y, w, h)
        fruit_rect = pygame.Rect(fruit_rect_size)

        screen.blit(self.apple, fruit_rect)

        # Draw the apple as an rectangle
        # pygame.draw.rect(screen, (126,166,114), fruit_rect)


    def randomize_position(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_game_over()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize_position()
            self.snake.add_block()

    def check_game_over(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        pygame.quit()
        sys.exit()

pygame.init()

cell_size = 30
cell_number = 20
dimensions = cell_number * cell_size

screen_size = (width, height) = dimensions, dimensions
screen = pygame.display.set_mode((screen_size))

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

clock = pygame.time.Clock()
framerate = 60

game = MAIN()
UP = Vector2(0,-1)
DOWN = Vector2(0, 1)
RIGHT = Vector2(1,0)
LEFT = Vector2(-1,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.snake.body[0] + UP != game.snake.body[1]:
                    game.snake.direction = UP
            if event.key == pygame.K_DOWN:
                if game.snake.body[0] + DOWN != game.snake.body[1]:
                    game.snake.direction = DOWN
            if event.key == pygame.K_RIGHT:
                if game.snake.body[0] + RIGHT != game.snake.body[1]:
                    game.snake.direction = RIGHT
            if event.key == pygame.K_LEFT:
                if game.snake.body[0] + LEFT != game.snake.body[1]:
                    game.snake.direction = LEFT
                
    screen.fill((175,215,70))
    game.draw_elements()
    pygame.display.update()
    clock.tick(framerate)