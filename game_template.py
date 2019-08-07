# This is a pygame template sceleton for a new pygame project
import pygame as pg
import random
import os
from settings import *


class Game:
    def __init__(self):
        # Initialise Game window and other things
        self.running = True
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

    def new(self):
        # Start a new game
        self.all_sprites = pg.sprite.Group()
        self.run()
        

    def run(self):
        # Game loop  
        # Process Input Events
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)  
            self.event()
            self.update()
            self.draw()

    def update(self):
        # Game loop update
        self.all_sprites.update()
    
    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    
    def draw(self):
        # Game loop draw
        # Render Draw
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        # After the drawing flip the screen to display
        pg.display.flip()
    
    def show_start_screen(self):
        pass
    
    def show_game_over_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_game_over_screen()

pg.quit()
