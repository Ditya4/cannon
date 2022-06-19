import pygame
from random import randint
import cannon as cannon_module
import targets as targets_module


def main():
    """ Cannon_x and cannon_y can't be 0 at one time. Error 200. Divising by Zero)
        red is red component in rgb color
    """
    cannon_x = 10
    cannon_y = -10
    cannon_width = 10
    cannon_height = 40
    red = 0
    default_red = red
    '''
               x, y, x_speed, y_speed, radius, color,
               left_top_border_x, left_top_border_y,
               right_bottom_border_x, right_bottom_border_y, surface)
    '''
    targets = []
    target_count = 5
    min_speed = -6
    max_speed = 6
    min_radius = 10
    max_radius = 25
    color = "yellow"
    left_top_border_x = 0
    left_top_border_y = WINDOW_HEIGHT // 2
    right_bottom_border_x = WINDOW_WIDTH
    right_bottom_border_y = WINDOW_HEIGHT
    run = True
    clock = pygame.time.Clock()
    pygame.init()
    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Cannon")
    cannon = cannon_module.Cannon(cannon_x, cannon_y, cannon_width,
                                  cannon_height, red, surface)
    for unused_number in range(target_count):
        radius = randint(min_radius, max_radius)
        targets.append(targets_module.Target(
                randint(left_top_border_x + radius,
                        right_bottom_border_x - radius),
                randint(left_top_border_y + radius,
                        right_bottom_border_y - radius),
                randint(min_speed, max_speed),
                randint(min_speed, max_speed),
                radius, color, left_top_border_x, left_top_border_y,
                right_bottom_border_x, right_bottom_border_y, surface))

    while run:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        surface.fill((0, 0, 0))

        condition = pygame.mouse.get_pressed(3)[0]
        print(condition)
        if condition:
            if red + 10 <= 244:
                red += 10
            cannon.color = (red, 70, 70)
        else:
            cannon.color = cannon.default_color
            red = default_red
        cannon.calculate_angle()
        unused_angle = cannon.draw_cannon()

        for target in targets:
            target.move()
            target.draw()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 650
    main()
