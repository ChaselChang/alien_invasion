class Settings():
    """the class restoring all settings for the alien_invasion"""
    
    def __init__(self):
        """initialize static settings"""
        
        # settings of screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # settings of the ship
        self.ship_limit = 3
        
        # setting of the bullet
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = (60, 60, 60)
        
        # setting of the alien
        self.fleet_drop_speed = 10
        
        
        # accelerate game in the speed of
        self.speedup_scale = 1.1
        # accelerate alien points
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """initialize dynamic settings"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        
        # fleet_direction=1 means move right, =-1 means move left
        self.fleet_direction = 1
        
        # scoring
        self.alien_points = 50
        
    def increase_speed(self):
        """increase the speed and alien points"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)