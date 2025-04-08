import pygame, sys

pygame.init()

screen_size = (width, height) = 400, 500
screen = pygame.display.set_mode((screen_size))

surface_size = (width, height) = 100, 200
test_surface = pygame.Surface((surface_size))

# rect_size = x, y, w, h = 100, 200, 50, 50
# test_rect = pygame.Rect(rect_size)
test_rect = test_surface.get_rect(center = (200,250))

screen.fill((175,215,70))
test_surface.fill('light blue')

clock = pygame.time.Clock()
framerate = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # pygame.draw.ellipse(screen, pygame.Color('red'), test_rect)
    screen.blit(test_surface,test_rect)
    pygame.display.update()
    clock.tick(framerate)