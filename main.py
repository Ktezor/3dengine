import pygame as pg

from camera import *
from object_3d import *
from projection import *

from settings_object import get_object

class Application(object):
  def __init__(self) -> None:
    pg.init()
    self.RES = self.WIDTH, self.HEIGHT = 1600, 900
    self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
    self.FPS = 60 ## lock FPS
    self.screen = pg.display.set_mode(self.RES)
    self.clock = pg.time.Clock()
    self.objects = []
    self.create_objects()

  def create_objects(self) -> None:
    self.camera = Camera(self, [-5.0, 6.0, -55.0])
    self.projection = Projection(self)

    for obj in get_objects(self):
      self.objects.append(obj)

  def draw(self) -> None:
    while True:
      self.draw()
      [exit() for i in pg.event.get() if i.type == pg.QUIT]
      pg.display.set_caption(str(self.clock.get_fps()))
      pg.display.flip()
      self.clock.tick(self.FPS)

## If isn't import
if __name__ == "__main__":
  app = Application()
  app.run()
