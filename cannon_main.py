import pygame
import cannon as cannon_module


def main():
    """ Cannon_x and cannon_y can't be 0 at one time. Error 200. Divising by Zero)
    """
    cannon_x = 40
    cannon_y = 40
    cannon_width = 10
    cannon_height = 40
    cannon_color = "maroon"
    run = True
    clock = pygame.time.Clock()
    pygame.init()
    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Cannon")
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        surface.fill((0, 0, 0))
        cannon = cannon_module.Cannon(cannon_x, cannon_y, cannon_width,
                                      cannon_height, cannon_color, surface)
        print(cannon.calculate_angle())
        angle = cannon.draw_cannon()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 650
    main()
