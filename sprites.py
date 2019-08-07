# Sprite classes for platform game
import pygame
from settings import *

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill(YELLOW)
        self.game = game
        self.rect = self.image.get_rect()
        self.position = vec(WIDTH/2, HEIGHT/2)
        self.velocity = vec(0, 0)
        self.acceleration = vec(0, 0)
        self.friction = PLAYER_FRICTION
        self.rect.midbottom = self.position

    def update(self):
        self.acceleration = vec(0, GRAVITY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x -= PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            self.acceleration.x += PLAYER_ACC

        # Adjust the acceleration by friction
        # The faster you go the more friction applies
        self.acceleration.x += self.velocity.x * self.friction
        self.acceleration.y += self.velocity.y * AIR_FRICTION
        # Standard equations for motion
        self.velocity += self.acceleration
        self.position += self.velocity + PLAYER_ACC * self.acceleration
        # Do not exit the screen
        if self.position.x > WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = WIDTH
        # Set new position
        self.rect.midbottom = self.position

    def jump(self):
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms_group, False)
        self.rect.y -= 1
        if hits:
            self.velocity.y = -20


class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
