import pygame
import random
import math

background_colour = (255,255,255)
(width, height) = (600, 600)

class Particle():
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 1
        self.speed = 0
        self.angle = 0

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

    def bounce(self):
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle

        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle

        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi/2 - self.angle

        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi/2 - self.angle

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 5')


particle = Particle(200, 200, 15)
particle.speed = 0.05
particle.angle = 3


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)

    
    particle.move()
    particle.bounce()
    particle.display()

    pygame.display.flip()