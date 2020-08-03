import pygame
import os

img_patch = os.path.join('Spongebob.png')

class character(object):
    def __init__(self):


      character.image = pygame.image.load('Spongebob.png')
      self.image = character.image

      self.x = 50
      self.y = 50
      self.hitbox = (self.x,self.y,55,55)
    def draw(self,surface):
      surface.blit(self.image,(self.x,self.y))

    def move(self):
     if event.K_DOWN:
        if event.key[pygame.K_LEFT]:
          self.x -= 1 
        if event.key[pygame.K_RIGHT]:
          self.x -= 1 
        if event.key[pygame.K_UP]: 
          self.x -= 1 
        if event.key[pygame.K_DOWN]:
          self.x -= 1




pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

Sprite = character()
clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False 



  screen.fill((255,255,255))
  Sprite.draw(screen)

  pygame.display.update()

  clock.tick()

def movement():

  while True:
    

    pygame.display.update()



