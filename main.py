import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.grow_snake = False

        self.UP = Vector2(0,-1)
        self.DOWN = Vector2(0,1)
        self.RIGHT = Vector2(1,0)
        self.LEFT = Vector2(-1,0)

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

        self.crunch_sound = pygame.mixer.Sound('./Sound/crunch.wav')

    def draw_snake(self):
        for index, block in enumerate(self.body):
            x = int(block.x * cell_size)
            y = int(block.y * cell_size)
            w = h = cell_size
            snake_rect_size = (x, y, w, h)
            snake_rect = pygame.Rect(snake_rect_size)

            if index == 0:
                self.update_head_graphics(snake_rect)
            elif index == len(self.body) - 1:
                self.update_tail_graphics(snake_rect)
            else:
                self.update_body_graphics(snake_rect, index, block)
            
    def update_head_graphics(self, rect):
        head_relation = self.body[0] - self.body[1]
        if head_relation == self.UP: screen.blit(self.head_up, rect)
        elif head_relation == self.DOWN: screen.blit(self.head_down, rect)
        elif head_relation == self.RIGHT: screen.blit(self.head_right, rect)
        elif head_relation == self.LEFT: screen.blit(self.head_left, rect)
                
    def update_tail_graphics(self, rect):
        tail_relation = self.body[-1] - self.body[-2]
        if tail_relation == self.UP: screen.blit(self.tail_up, rect)
        elif tail_relation == self.DOWN: screen.blit(self.tail_down, rect)
        elif tail_relation == self.RIGHT: screen.blit(self.tail_right, rect)
        elif tail_relation == self.LEFT: screen.blit(self.tail_left, rect)

    def update_body_graphics(self, rect, index, block):
        previous_block = self.body[index + 1] - block
        next_block = self.body[index - 1] - block
        if previous_block.x == next_block.x: screen.blit(self.body_vertical, rect)
        elif previous_block.y == next_block.y: screen.blit(self.body_horizontal, rect)
        else: self.update_body_corner_graphics(previous_block, next_block, block, rect)
    
    def update_body_corner_graphics(self, previous_block, next_block, block, rect):
        if next_block.x == -1 and previous_block.y == -1 or next_block.y == -1 and previous_block.x == -1: screen.blit(self.body_tl, rect)
        elif next_block.x == 1 and previous_block.y == 1 or next_block.y == 1 and previous_block.x == 1: screen.blit(self.body_br, rect)
        elif next_block.x == 1 and previous_block.y == -1 or next_block.y == -1 and previous_block.x == 1: screen.blit(self.body_tr, rect)
        elif next_block.x == -1 and previous_block.y == 1 or next_block.y == 1 and previous_block.x == -1: screen.blit(self.body_bl, rect)
        
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

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)

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

    def randomize_position(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.game_font = pygame.font.Font('./Font/PoetsenOne-Regular.ttf', 25)

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_game_over()

    def draw_elements(self):
        screen.fill((175,215,70))
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def draw_menu_screen(self):
        screen.fill((175,215,70))
        self.draw_grass()
        game_name_surf = self.game_font.render('Snake', True, (56, 74, 12))

        x = int(cell_size * cell_number / 2)
        y = cell_size * cell_number / 4.5

        game_name_rect = game_name_surf.get_rect(center = (x, y))
        screen.blit(game_name_surf, game_name_rect)


    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize_position()
            self.snake.add_block()
            self.snake.play_crunch_sound()

            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize_position()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        x = int(col * cell_size)
                        y = int(row * cell_size)
                        w = h = cell_size
                        grass_rect_size = (x, y, w, h)
                        grass_rect = pygame.Rect(grass_rect_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        x = int(col * cell_size)
                        y = int(row * cell_size)
                        w = h = cell_size
                        grass_rect_size = (x, y, w, h)
                        grass_rect = pygame.Rect(grass_rect_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        # The score is the snake body's length minus three, it's base size 
        score = str(len(self.snake.body) - 3)
        score_surface = self.game_font.render(f'Score: {score}', True, (56, 74, 12))

        x = int(cell_size * cell_number - 60)
        y = int(cell_size * cell_number - 20)

        score_rect = score_surface.get_rect(center = (x, y))
        screen.blit(score_surface, score_rect)

    def check_game_over(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        self.snake.reset()

pygame.mixer.pre_init(44100, -16, 2, 512)
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

menu_screen = True
run_game = False
game_over_screen = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.snake.body[0] + game.snake.UP != game.snake.body[1]:
                    game.snake.direction = game.snake.UP
            if event.key == pygame.K_DOWN:
                if game.snake.body[0] + game.snake.DOWN != game.snake.body[1]:
                    game.snake.direction = game.snake.DOWN
            if event.key == pygame.K_RIGHT:
                if game.snake.body[0] + game.snake.RIGHT != game.snake.body[1]:
                    game.snake.direction = game.snake.RIGHT
            if event.key == pygame.K_LEFT:
                if game.snake.body[0] + game.snake.LEFT != game.snake.body[1]:
                    game.snake.direction = game.snake.LEFT

    if menu_screen:
        game.draw_menu_screen()
        pygame.display.update()
        clock.tick(framerate)

    elif run_game:   
        game.draw_elements()
        pygame.display.update()
        clock.tick(framerate)

    elif game_over_screen:
        pass
        