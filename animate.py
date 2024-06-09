import pygame
import sys

def animate_points(positions, velocity, iteration):

    pygame.init()

    WIDTH, HEIGHT = 800, 600
    BG_COLOR = (0, 0, 0)
    BLUE = (0, 0, 255) 
    YELLOW = (255, 255, 0)
    POINT_RADIUS = 5
    STAR_POINT = 10
    screen_width = 800
    screen_height = 600

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    scale_factor=1e9
    i = 0
    while i < iteration:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # for planet_name, position_list in positions.items():
            
        #     x = [pos[0] / scale_factor + screen_width / 2 for pos in position_list]
        #     y = [pos[1] / scale_factor + screen_height / 2 for pos in position_list]

        #     pygame.draw.circle(screen, YELLOW, (WIDTH // 2, HEIGHT // 2), STAR_POINT)
        #     pygame.draw.circle(screen, BLUE, (x, y), 5)
        #     pygame.display.flip()
        #     clock.tick(100)
        for planet_name, position_list in positions.items():
            for pos in position_list:
                x = int(pos[0] / scale_factor + screen_width / 2)
                y = int(pos[1] / scale_factor + screen_height / 2)
                

                pygame.draw.circle(screen, YELLOW, (WIDTH // 2, HEIGHT // 2), STAR_POINT)
                pygame.draw.circle(screen, BLUE, (x, y), 5)
                pygame.display.flip()
                clock.tick(100)

        i+=1


