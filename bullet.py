import pygame


class Bullet:

    def __init__(self, x, y, x_speed, y_speed, radius, color, surface):
        """
            color will be same as power cannon color
        """
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.radius = radius
        self.color = color
        self.surface = surface

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y),
                           self.radius)
