import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """a class representing single alien"""
    
    def  __init__(self, ai_settings, screen):
        """initialize alien and set their initial position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # load alien image and set its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # every alien born at left-upward the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # restore exact positon of alien
        self.x = float(self.rect.x)
        
    def blitme(self):
        """paint alien at specific position"""
        self.screen.blit(self.image, self.rect)
        
    def check_edges(self):
        """if aliens are on the edge of the screen return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
            
    def update(self):
        """move alien leftwards or rightwards"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x