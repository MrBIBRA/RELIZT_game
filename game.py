import pygame
from random import randint

pygame.init()

back = (200, 200, 200)

clock = pygame.time.Clock()
mw = pygame.display.set_mode((500,500))
mw.fill(back)

class Area():
    def __init__(self, x=0,y=0, width=10, height=10, color=None ):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = back
        if color:
            self.fill_color = colo
    def color(self,new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x,y)
    def colliderect(self,rect):
        return self.rect.colliderect(rect)
class Picture(Area):
    def __init__(self,filename, x = 0, y = 0,width=10, height=10):
        Area.__init__(self, x = x, y = y, width = width, height = height, color = None)
        self.image = pygame.image.load(filename)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont("verdana" , fsize).render(text, True, text_color)
    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

geme_over = False

while not geme_over:
    pygame.display.update()
    clock.tick(40)

