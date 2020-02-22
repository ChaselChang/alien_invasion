import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class managing bullets"""
    
    def __init__(self, ai_settings, screen, ship):
        """creat a bullet object at ship position"""
        super().__init__()
        self.screen = screen
        
        # creat a rectangel representing bullet and give it a right position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # restoring bullet position in floating number
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """move bullet upwards"""
        # refresh the floating number representing bullet pisition
        self.y -= self.speed_factor
        # refresh the rect position
        self.rect.y = self.y
        
    def draw_bullet(self):
        """draw a bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)