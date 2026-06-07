import arcade

class Coin(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(":resources:images/items/gold_1.png", 0.4)
        self.center_x = x
        self.center_y = y

    def update(self, delta_time: float = 1/60):
        # Optional: Add a small floating animation here
        pass