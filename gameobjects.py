#*- coding: utf-8 -*-  
# The initial game characters were based on Robots, and a robot named Botley and a falling weight, so the name confusions might be apparent throughout the program's .py files
import pygame,config,os
from random import randrange
import random


class RobotSprite(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
                                            
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        shrink = -config.margin * 2
        self.area = screen.get_rect().inflate(shrink,shrink)
class Weight(RobotSprite):
    
    def __init__(self,speed):
        currentweight = random.choice(config.weightimages)
        RobotSprite.__init__(self, currentweight)
        self.speed = speed
        self.reset()
    def reset(self):
        x = randrange(self.area.left, self.area.right)
        self.rect.midbottom = x,0
        
    def update(self):
        
        self.rect.top += self.speed
        self.landed = self.rect.top >= self.area.bottom
    
class Botley(RobotSprite):
    def __init__(self):
        currentplayer = random.choice(config.player)
        RobotSprite.__init__(self, currentplayer)
        self.rect.bottom  = self.area.bottom
        self.pad_top = config.botley_pad_top
        self.pad_side = config.botley_pad_side
    def update(self):
        
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect = self.rect.clamp(self.area)
    def touches(self,other):
        bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
        bounds.bottom = self.rect.bottom
        return bounds.colliderect(other.rect)
# The following class is pointless for there is no ingame implementation of it.
# Thought that in future a hud might be a welcome addition and voila there we have it.
class HUD(RobotSprite):

    def __init__(self):
        RobotSprite.__init__(self, config.HUD)
        self.dodges = 0
        self.score = 0
        self.lives = 1
        self.font = pygame.font.SysFont("None", 30)
        
                
    def update(self):
        self.text = "Escapes: %d" % (self.dodges) + str(" Lives: %d") % (self.lives)
        black = (0,0,0)
        self.image = self.font.render(self.text, 1, black)
        self.rect = self.image.get_rect()    
            
