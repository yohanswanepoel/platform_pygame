# Sprite classes for platform game
import pygame
from settings import *

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):



    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.position = vec(WIDTH/2, HEIGHT/2)
        self.velocity = vec(0, 0)
        self.acceleration = vec(0, 0)
        self.rect.center = self.position
        self.friction = PLAYER_FRICTION

    def update(self):
        self.acceleration = vec(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x -= PLAYER_ACC
        if keys[pygame.K_RIGHT]:
            self.acceleration.x += PLAYER_ACC

        # Adjust the acceleration by friction
        # The faster you go the more friction applies
        self.acceleration += self.velocity * self.friction
        # Standard equations for motion
        self.velocity += self.acceleration
        self.position += self.velocity + PLAYER_ACC * self.acceleration
        # Do not exit the screen
        if self.position.x > WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = WIDTH
        # Set new position
        self.rect.center = self.position


