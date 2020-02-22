class GameStats():
    """follow data information of game"""
    
    def __init__(self, ai_settings):
        """initialize data information"""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # deactive when game starts
        self.game_active = False
        
        # under no circumstance initialize the highest score
        self.high_score = 0
        
    def reset_stats(self):
        """initialize flexible data information"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1