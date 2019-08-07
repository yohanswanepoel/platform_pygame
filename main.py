# This is a pygame template sceleton for a new pygame project
import pygame as pg
import random
import os
from settings import *
from sprites import *


class Game:
    def __init__(self):
        # Initialise Game window and other things
        self.running = True
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.all_sprites = None
        self.platforms_group = None
        self.player = None
        self.playing = False

    def new(self):
        # Start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms_group = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for p in PLATFORM_LIST:
            platform = Platform(*p)
            self.platforms_group.add(platform)
            self.all_sprites.add(platform)
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
        # Check if player hits a platform only if falling
        if self.player.velocity.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms_group, False)
            if hits:
                self.player.position.y = hits[0].rect.top
                self.player.velocity.y = 0  # Tell the player it is standing on a platform

        # If Player is top 3/4 of screen move
        if self.player.rect.top < HEIGHT / 4:
            self.player.position.y += abs(self.player.velocity.y)
            for plat in self.platforms_group:
                plat.rect.y += abs(self.player.velocity.y)
                if plat.rect.top > HEIGHT:
                    plat.kill()
                    self.new_platform()

        # if self.player.rect.bottom > (HEIGHT / 4) * 3:
        #    self.player.position.y -= abs(self.player.velocity.y)
        #    for plat in self.platforms_group:
        #        plat.rect.y -= abs(self.player.velocity.y)

    def new_platform(self):
        width = random.randrange(50,120)
        height = 20
        x = random.randrange(0, WIDTH - width)
        y = random.randrange(-75, -30)
        p = Platform(x, y, width, height)
        self.all_sprites.add(p)
        self.platforms_group.add(p)

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    
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



# SET The assets folder
# game_folder = os.path.dirname(__file__) # gives us the folder that this file is running from
# img_folder = os.path.join(game_folder, 'img')

