import pygame
import sys
import time
import random

from pygame.locals import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800

WHITE = (255,255,255)
GREEN = (0,100,0)
ORANGE = (0,150,150)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

GRID_SIZE = 20
GRID_WIDHTH = WINDOW_WIDTH / GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT/ GRID_SIZE

FPS = 10
class Python(object):
     def __init__(self):
          self.create()
          self.color = GREEN

     def create(self) :
          self.length = 2 #뱀길이
          self.positions = [((WINDOW_WIDTH/2),(WINDOW_HEIGHT/2))] # 처음위치 지정 중아에
          self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

     def control(self, xy):
          if(xy[0] * -1, xy[1] * -1) == self.direction:
               return
          else:
               self.direction = xy
     def move(self):
         cur = self.positions[0] # 뱀의머리
         x, y = self.direction
         new = (((cur[0] + (x * GRID_SIZE)) % WINDOW_WIDTH), (cur[1] + (y * GRID_SIZE)) % WINDOW_HEIGHT)
         if new in self.positions[2:]:
              self.create()
         else :
              self.positions.insert(0, new)
              if len(self.positions) > self.length:
                   self.positions.pop()

     def eat(self):
          self.length += 5

     def draw(self, surface):
          for p in self.positions:
               draw_object(surface, self.color, p)

class Feed(object):
     def __init__(self):
          self.position = (0,0)
          self.color = ORANGE
          self.create()
     def create(self):
          self.position = (random.randint(0, GRID_WIDHTH -1) * GRID_SIZE,random.randint(0,GRID_HEIGHT -1) * GRID_SIZE)

     def draw(self,surface):
          draw_object(surface,self.color, self.position)
def draw_object(surface, color , pos):
     r = pygame.Rect((pos[0],pos[1]),(GRID_SIZE,GRID_SIZE))
     pygame.draw.rect(surface,color,r)


def check_eat(python,feed):
     if python.positions[0] == feed.position:
          python.eat()
          feed.create()

if __name__ == '__main__':

          python = Python()
          feed = Feed()

          pygame.init()
          window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), 0, 32)
          pygame.display.set_caption('eat_my_tail')
          surface = pygame.Surface(window.get_size())
          surface.fill(WHITE)
          clock = pygame.time.Clock()
          pygame.key.set_repeat( 1, 40)
          window.blit(surface,(0,0))

          while True:

               for event in pygame.event.get():
                    if event.type == QUIT:
                         pygame.quit()
                         sys.exit()
                    elif event.type == KEYDOWN:
                         if event.key == K_UP:
                              python.control(UP)
                         elif event.key ==K_DOWN:
                              python.control(DOWN)
                         elif event.key ==K_LEFT:
                              python.control(LEFT)
                         elif event.key ==K_RIGHT:
                              python.control(RIGHT)
               surface.fill(WHITE)
               python.move()
               check_eat(python,feed)
               speed = (FPS + python.length)
               python.draw(surface)
               feed.draw(surface)
               window.blit(surface,(0,0))
               pygame.display.flip()
               pygame.display.update()
               clock.tick(speed)
