import arcade

class Platform(arcade.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        # Creating a simple colored texture
        self.texture = arcade.make_soft_square_texture(size=50, color=(76, 153, 0), outer_alpha=255)
        self.width = width
        self.height = height
        self.center_x = x
        self.center_y = y