import os,sys,pygame
from pygame.locals import *
import gameobjects, config
import random




class GameState:
    
    def handle(self,event):
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
            
    def firstDisplay(self, screen):
        screen.fill(config.background_colour)
        pygame.display.flip()
    
    def display(self,screen):
        pass

class Level(GameState):
    def __init__(self, number = 1):
        self.number = number
        self.remaining = config.weights_per_level
        
        speed = config.drop_speed
        speed += (self.number-1) * config.speed_increase
        
        self.weight = gameobjects.Weight(speed)
        self.botley = gameobjects.Botley()
        both = self.weight, self.botley
        self.sprites = pygame.sprite.RenderUpdates(both)
    def update(self, game):
        self.sprites.update()
        
        if self.botley.touches(self.weight):
            pygame.mixer.init()
            pygame.mixer.Sound(config.soundfile).play()
                   
            
            game.nextState = GameOver()
        elif self.weight.landed:
            self.weight.reset()
            sounds = random.choice(config.escapesounds)
            pygame.mixer.init()
            pygame.mixer.Sound(sounds).play()
            self.remaining -= 1
            if self.remaining == 0:
                game.nextState = LevelCleared(self.number)
    def display(self,screen):
        screen.fill(config.background_colour)
        updates = self.sprites.draw(screen)
        pygame.display.update(updates)
        
class Paused(GameState):
    
    finished = 0
    image = config.gamepaused
    # add your own text below
    text = '' 
    def handle(self,event):
        GameState.handle(self, event)
        if event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
            self.finished = 1
    def update(self,game):
        if self.finished:
            game.nextState = self.nextState()
            
    def firstDisplay(self,screen):
        screen.fill(config.background_colour)
        font = pygame.font.init()
        font = pygame.font.Font(None, config.font_size)
        lines = self.text.strip().splitlines()
        
        height = len(lines) * font.get_linesize()
        
        center,top = screen.get_rect().center
        top -= height // 2
        
        if self.image:
            
            image = pygame.image.load(self.image).convert()
            r = image.get_rect()
            top += r.height //2
            r.midbottom = center, top-20
            screen.blit(image,r)
            
        antialias = 1
        black = 0, 0, 0
        
        for line in lines:
            text = font.render(line.strip(), antialias, black)
            r = text.get_rect()
            r.midtop = center,top
            screen.blit(text,r)
            top += font.get_linesize()
            
        pygame.display.flip()
        
class Information(Paused):
    image = config.ready
    nextState = Level
    # insert whatever text you want below
    text = ''' \n\n'''
    pygame.mixer.init()
    pygame.mixer.Sound(config.cry).play()
class StartUp(Paused):
    nextState = Information
    image = config.startupimage
    text = "zomgevadeOverlawd\n\n Evade the Wakoopa Overlawd, Meh Guy!"
    
class LevelCleared(Paused):
    def __init__(self,number):
        self.number = number
        self.text = 'Levels cleared: %d' % self.number
        sounds2 = random.choice(config.gameoversounds)
        pygame.mixer.init()
        pygame.mixer.Sound(sounds2).play()
        
    def nextState(self):        
        return Level(self.number+1)
class GameOver(Paused):
    
    image = config.out
    nextState = Level
    
    text = "Aw shucks :( Click me?"
    
class Game:
    def __init__(self,*args):
        path = os.path.abspath(args[0])
        dir = os.path.split(path)[0]
        os.chdir(dir) 
        self.state = None
        self.nextState = StartUp()
    def run(self):
        flag = 0
        if config.full_screen:
            flag = FULLSCREEN
        screen_size = config.screen_size
        screen = pygame.display.set_mode(screen_size,flag)
        pygame.display.set_caption('LOLZORS')
        pygame.mouse.set_visible(True)
        while True:
            #if self.state != self.nextState:
                self.state = self.nextState
                self.state.firstDisplay(screen)
                for event in pygame.event.get():
                    self.state.handle(event)
                self.state.update(self)
                self.state.display(screen)
                
            
                
if __name__ == '__main__':
    game = Game(*sys.argv)
    game.run()
