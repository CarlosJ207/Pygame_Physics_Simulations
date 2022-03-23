import pygame


#Changing the window's properties
background_color = (255,255,255)
(width, height) = (500, 300)


#Initializing the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_color)


#Starting the window
pygame.display.flip()


#Closing the window
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False