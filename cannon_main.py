import pygame
from random import randint
import cannon as cannon_module
import target as targets_module
import bullet as bullet_module


def main():
    """ Cannon_x and cannon_y can't be 0 at one time. Error 200. Divising by Zero)
        red is red component in rgb color
    """
    cannon_x = 10
    cannon_y = 10
    cannon_width = 10
    cannon_height = 40
    red = 0
    default_red = red
    '''
               x, y, x_speed, y_speed, radius, color,
               left_top_border_x, left_top_border_y,
               right_bottom_border_x, right_bottom_border_y, surface)
               bullet_speed_x відноситься до bullet_speed_y як відноситься
               кут angle до 90 - angle градусів
    '''
    targets = []
    target_count = 5
    target_current_count = 0
    target_min_speed = -6
    target_max_speed = 6
    target_min_radius = 10
    target_max_radius = 25
    target_color = "yellow"
    left_top_border_x = 0
    left_top_border_y = WINDOW_HEIGHT // 2
    right_bottom_border_x = WINDOW_WIDTH
    right_bottom_border_y = WINDOW_HEIGHT
    bullet_x = 30
    bullet_y = 30
    bullet_x_speed = None
    bullet_y_speed = None
    bullet_power = None
    bullet_radius = cannon_width
    bullet_color = None
    bullets = []
    run = True
    charging_bullet = False
    clock = pygame.time.Clock()
    pygame.init()
    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Cannon")
    cannon = cannon_module.Cannon(cannon_x, cannon_y, cannon_width,
                                  cannon_height, red, surface)
    for unused_number in range(target_count):
        radius = randint(target_min_radius, target_max_radius)
        targets.append(targets_module.Target(
                randint(left_top_border_x + radius,
                        right_bottom_border_x - radius),
                randint(left_top_border_y + radius,
                        right_bottom_border_y - radius),
                randint(target_min_speed, target_max_speed),
                randint(target_min_speed, target_max_speed),
                radius, target_color, left_top_border_x, left_top_border_y,
                right_bottom_border_x, right_bottom_border_y, surface))

    while run:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        surface.fill((0, 0, 0))

        cannon.calculate_angle()
        angle = cannon.draw_cannon()
        if len(targets) == 0:
            print(len(bullets))
            # don't know why, but it removes only half of bullets at once ((
            while bullets:
                for bullet in bullets:
                    bullets.remove(bullet)
            print(len(bullets))
            for unused_number in range(target_count):
                # radius = randint(target_min_radius, target_max_radius)
                targets.append(targets_module.Target(
                             randint(left_top_border_x + radius,
                                     right_bottom_border_x - radius),
                             randint(left_top_border_y + radius,
                                     right_bottom_border_y - radius),
                             randint(target_min_speed, target_max_speed),
                             randint(target_min_speed, target_max_speed),
                             radius, target_color, left_top_border_x,
                             left_top_border_y, right_bottom_border_x,
                             right_bottom_border_y, surface))

        for target in targets:
            target.move()
            target.draw()
        left_mouse_pressed = pygame.mouse.get_pressed(3)[0]
        if left_mouse_pressed:
            charging_bullet = True
            if red + 10 <= 244:
                red += 10
            cannon.color = (red, 70, 70)
        else:
            if charging_bullet:
                bullet_power = red // 10
                # can't create a proper math model, take aproximately
                if angle < 18:
                    coeficient = angle / (90 - angle)
                else:
                    coeficient = angle / (180 - angle)

                bullet_x_speed = bullet_power * coeficient
                bullet_y_speed = bullet_power * (1 - coeficient)
                print(angle, coeficient + coeficient, bullet_x_speed,
                      bullet_y_speed)
                bullets.append(bullet_module.Bullet(bullet_x, bullet_y,
                                                    bullet_x_speed,
                                                    bullet_y_speed,
                                                    radius, cannon.color,
                                                    surface))
                charging_bullet = False
            cannon.color = cannon.default_color
            red = default_red
        for bullet in bullets:
            for target in targets:
                if target.check_collision(bullet):
                    targets.remove(target)
                    bullets.remove(bullet)
            if (-bullet.radius > bullet.x or
                    bullet.x > WINDOW_WIDTH + bullet.radius or
                    -bullet_radius > bullet.y or
                    bullet.y > WINDOW_HEIGHT + bullet.radius):
                bullets.remove(bullet)
                print(len(bullets))
            bullet.move()
            bullet.draw()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 650
    main()
