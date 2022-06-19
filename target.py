import pygame


class Target:

    def __init__(self, x, y, x_speed, y_speed, radius, color,
               left_top_border_x, left_top_border_y,
               right_bottom_border_x, right_bottom_border_y, surface):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.radius = radius
        self.color = color
        self.left_top_border_x = left_top_border_x
        self.left_top_border_y = left_top_border_y
        self.right_bottom_border_x = right_bottom_border_x
        self.right_bottom_border_y = right_bottom_border_y
        self.surface = surface

    def move(self):
        """
            moving targets inside border area and hitting back from the borders
        """
        if self.left_top_border_x < self.x + self.x_speed < (
                self.right_bottom_border_x):
            self.x += self.x_speed
        else:
            self.x_speed *= -1
        if self.left_top_border_y < self.y + self.y_speed < (
                self.right_bottom_border_y):
            self.y += self.y_speed
        else:
            self.y_speed *= -1

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y),
                           self.radius)
