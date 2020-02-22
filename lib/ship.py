import pygame

from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """initialize the ship and set its original position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #load the ship image and obtain its circumscribed rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # put new ship middle the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # restore floating number in center property of the ship
        self.center = float(self.rect.centerx)
        
        # moving mark
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """adjust position of ship according to the moving mark"""
        # refresh the value of center of ship instead of rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # refresh the rect object according to self.center
        self.rect.centerx = self.center
        
    def blitme(self):
        """paint a ship on the specified position"""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """make the ship center the screen bottom"""
        self.center = self.screen_rect.centerx