import pygame
from math import acos, pi


class Cannon:

    def __init__(self, x, y, width, height, color, surface):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.surface = surface

    def calculate_angle(self):
        """ first vector = {self.x, self.y; self.x + 50, self.y}
            second vector = {self.x, self.y; mouse_x, mouse_y}
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        print(mouse_x, mouse_y, " ", end="")
        first_point_first_vector_x = self.x
        first_point_first_vector_y = self.y
        second_point_first_vector_x = self.x + 1
        second_point_first_vector_y = self.y
        first_point_second_vector_x = self.x
        first_point_second_vector_y = self.y
        second_point_second_vextor_x = mouse_x
        second_point_second_vextor_y = mouse_y
        angle = find_angle(first_point_first_vector_x,
                           first_point_first_vector_y,
                           second_point_first_vector_x,
                           second_point_first_vector_y,
                           first_point_second_vector_x,
                           first_point_second_vector_y,
                           second_point_second_vextor_x,
                           second_point_second_vextor_y)
        return angle

    def power_up(self):
        pass

    def shoot(self):
        pass

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
                          rotated_surf.get_rect(center=target_rect.center))


def find_angle(first_a_x, first_a_y, first_b_x, first_b_y,
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
    cos_alpha = scalar_product / (first_length * second_length)
    alpha_in_radian= acos(cos_alpha)
    alpha = alpha_in_radian * (180 / pi)
    #convert
    alpha = 90 - alpha
    return alpha














