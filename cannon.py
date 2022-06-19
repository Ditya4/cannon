import pygame
from math import acos, pi, atan, cos, sin


class Cannon:

    def __init__(self, x, y, width, height, red, surface):
        """ in case of refactoring wannity:
            KISS cannon could be a line with width. lol
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.default_height = height
        self.red = red
        self.color = (red, 70, 70)
        self.default_color = (red, 70, 70)
        self.surface = surface

    def calculate_angle_new(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x - self.x == 0:
            angle = atan((mouse_y - self.y) / 0.00001)
        else:
            angle = atan((mouse_y - self.y) / (mouse_x - self.x))
        print(angle)
        return angle

    

    def calculate_angle(self):
        """ first vector = {self.x, self.y; self.x + 50, self.y}
            second vector = {self.x, self.y; mouse_x, mouse_y}
            finding angle between Ox axis and vector from point (0, 0)
            to mouse position
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # print(mouse_x, mouse_y, " ", end="")
        first_point_first_vector_x = self.x
        first_point_first_vector_y = self.y
        second_point_first_vector_x = self.x + 1
        second_point_first_vector_y = self.y
        first_point_second_vector_x = self.x
        first_point_second_vector_y = self.y
        second_point_second_vextor_x = mouse_x
        second_point_second_vextor_y = mouse_y
        angle = _find_angle(first_point_first_vector_x,
                            first_point_first_vector_y,
                            second_point_first_vector_x,
                            second_point_first_vector_y,
                            first_point_second_vector_x,
                            first_point_second_vector_y,
                            second_point_second_vextor_x,
                            second_point_second_vextor_y)
        return angle

    def draw_cannon(self):
        rect = (self.x, self.y, self.width, self.height)
        angle = self.calculate_angle()
        self.draw_rect_angle(angle, rect)
        return angle

    def draw_rect_angle(self, angle, rect):
        target_rect = pygame.Rect(rect)
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, self.color, (0, 0, *target_rect.size))
        rotated_surf = pygame.transform.rotate(shape_surf, angle)
        self.surface.blit(rotated_surf,
                          rotated_surf.get_rect(center=(self.x, self.y)))


def _find_angle(first_a_x, first_a_y, first_b_x, first_b_y,
                second_a_x, second_a_y, second_b_x, second_b_y):
    """ coords of two vectors
        we steal calculating method from:
        https://ua.onlinemschool.com/math/assistance/vector/angl/
    """
    # finding vectors by point's coords:
    first_ab_x = first_b_x - first_a_x
    first_ab_y = first_b_y - first_a_y
    second_ab_x = second_b_x - second_a_x
    second_ab_y = second_b_y - second_a_y
    # finding scalar product of vectors:
    scalar_product = (first_ab_x * second_ab_x +
                      first_ab_y * second_ab_y)
    # finding length of vectors:
    first_length = (first_ab_x ** 2 + first_ab_y ** 2) ** 0.5
    second_length = (second_ab_x ** 2 + second_ab_y ** 2) ** 0.5
    # finding cos(angle)
    if first_length == 0 and second_length == 0:
        cos_alpha = scalar_product / 0.001
    else:
        cos_alpha = scalar_product / (first_length * second_length)
    alpha_in_radian = acos(cos_alpha)
    alpha = alpha_in_radian * (180 / pi)
    # convert
    alpha = 90 - alpha
    return alpha # , alpha_in_radian
