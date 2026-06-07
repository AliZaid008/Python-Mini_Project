import arcade
from constants import MOVE_SPEED, JUMP_SPEED, GRAVITY

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.center_x = 100
        self.center_y = 200
        self.is_on_ground = False

    def update(self, delta_time: float = 1/60):
        if not self.is_on_ground:
            self.change_y -= GRAVITY
        
        self.center_x += self.change_x
        self.center_y += self.change_y

    def move_left(self):
        self.change_x = -MOVE_SPEED

    def move_right(self):
        self.change_x = MOVE_SPEED

    def jump(self):
        if self.is_on_ground:
            self.change_y = JUMP_SPEED
            self.is_on_ground = False # Immediately set to false so you can't double-jump

    def stop_horizontal(self):
        self.change_x = 0

    def reset(self):
        self.center_x = 100
        self.center_y = 200
        self.change_x = 0
        self.change_y = 0