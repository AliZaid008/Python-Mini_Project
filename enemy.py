import arcade
from constants import ENEMY_SPEED

class Knife(arcade.Sprite):
    def __init__(self, x, y):
        # Uses a valid built-in arcade resource for a knife-like hazard
        super().__init__(":resources:images/items/coinGold.png", 0.8)
        self.color = arcade.color.PURPLE
        self.center_x = x
        self.center_y = y

    def update(self, delta_time: float = 1/60):
        # Rotate 5 degrees every frame
        self.angle += 5

class Enemy(arcade.Sprite):
    def __init__(self, x, y, boundary_left, boundary_right):
        super().__init__(":resources:images/enemies/slimeBlue.png", 0.5)
        self.center_x = x
        self.center_y = y
        self.boundary_left = boundary_left
        self.boundary_right = boundary_right
        self.change_x = ENEMY_SPEED

    # Add delta_time here to fix the TypeError
    def update(self, delta_time: float = 1/60):
        self.center_x += self.change_x
        
        # Patrol logic: Flip direction at boundaries
        if self.left < self.boundary_left:
            self.change_x *= -1
            self.left = self.boundary_left # Snap to boundary to prevent getting stuck
        elif self.right > self.boundary_right:
            self.change_x *= -1
            self.right = self.boundary_right # Snap to boundary