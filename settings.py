class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 10.0

        # Bullet settings
        self.bullet_speed = 7.0
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 rep. right and -1 rep. left
        self.fleet_direction = 1





