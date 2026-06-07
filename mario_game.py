import arcade
from constants import *
from player import Player
from game_platform import Platform
from coin import Coin
from enemy import Enemy, Knife
from game_state import GameState

class Mario_Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.background_color = arcade.color.SKY_BLUE
        self.game_state = GameState()
        
        self.player_list = None
        self.platforms = None
        self.enemy_list = None
        self.goal_list = None 
        self.coin_list = None
        self.player = None
        self.camera = None
        self.coins_collected_this_level = 0

    def setup(self):
        print(f"--- Loading Level {self.game_state.level} ---")
        self.player_list = arcade.SpriteList()
        self.platforms = arcade.SpriteList(use_spatial_hash=True)
        self.enemy_list = arcade.SpriteList()
        self.goal_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.camera = arcade.camera.Camera2D()
        self.coins_collected_this_level = 0

        self.player = Player()
        self.player.center_x = 100
        self.player.center_y = 150
        self.player_list.append(self.player)

        lvl = self.game_state.level
        
        if lvl == 1:
            self.platforms.append(Platform(400, 20, 800, 40))
            self.platforms.append(Platform(600, 100, 180, 20))
            self.add_coin(450, 60)
            self.add_coin(620, 140)
            self.add_goal(700, 130)
        elif lvl == 2:
            self.platforms.append(Platform(400, 20, 800, 40))
            self.platforms.append(Platform(320, 120, 160, 20))
            self.platforms.append(Platform(600, 180, 160, 20))
            self.enemy_list.append(Enemy(500, 65, 420, 580))
            self.add_coin(340, 160)
            self.add_coin(620, 240)
            self.add_goal(720, 220)
        elif lvl == 3:
            self.platforms.append(Platform(250, 20, 500, 40))
            self.platforms.append(Platform(520, 110, 160, 20))
            self.platforms.append(Platform(820, 170, 160, 20))
            self.platforms.append(Platform(1120, 230, 160, 20))
            self.enemy_list.append(Enemy(380, 65, 340, 460))
            self.enemy_list.append(Enemy(820, 195, 780, 860))
            self.add_coin(300, 80)
            self.add_coin(620, 160)
            self.add_coin(900, 240)
            self.add_goal(1180, 260)
        elif lvl == 4:
            self.platforms.append(Platform(300, 20, 700, 40))
            self.platforms.append(Platform(520, 120, 180, 20))
            self.platforms.append(Platform(820, 190, 180, 20))
            self.platforms.append(Platform(1120, 260, 180, 20))
            self.enemy_list.append(Enemy(420, 65, 380, 520))
            self.enemy_list.append(Enemy(780, 215, 740, 860))
            self.enemy_list.append(Knife(1080, 310))
            self.add_coin(560, 160)
            self.add_coin(860, 250)
            self.add_coin(1160, 330)
            self.add_goal(1170, 300)
        elif lvl == 5:
            self.platforms.append(Platform(320, 20, 620, 40))
            self.platforms.append(Platform(560, 120, 180, 20))
            self.platforms.append(Platform(860, 190, 180, 20))
            self.platforms.append(Platform(1160, 260, 180, 20))
            self.enemy_list.append(Enemy(380, 65, 340, 460))
            self.enemy_list.append(Enemy(760, 215, 720, 820))
            self.enemy_list.append(Knife(1120, 310))
            self.add_coin(560, 160)
            self.add_coin(860, 250)
            self.add_coin(1160, 330)
            self.add_goal(1170, 300)

    def add_coin(self, x, y):
        coin = Coin(x, y)
        self.coin_list.append(coin)

    def add_goal(self, x, y):
        goal = arcade.Sprite(":resources:images/items/flagGreen1.png", 0.5)
        goal.center_x, goal.center_y = x, y
        self.goal_list.append(goal)

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.platforms.draw()
        self.enemy_list.draw()
        self.coin_list.draw()
        self.goal_list.draw()
        self.player_list.draw()
        arcade.camera.Camera2D().use()
        self.draw_ui()

    def draw_ui(self):
        score_text = f"Score: {self.game_state.score} | Coins: {self.coins_collected_this_level} | Level: {self.game_state.level}/5 | Lives: {self.game_state.lives}"
        arcade.draw_text(score_text, 20, SCREEN_HEIGHT - 40, arcade.color.WHITE, 14)
        if self.game_state.game_over:
            arcade.draw_text("GAME OVER", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 80, arcade.color.RED, 50, anchor_x="center")
            self.draw_restart_button()
            arcade.draw_text("Click Restart, press R to restart, or press Q to quit", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 80, arcade.color.WHITE, 18, anchor_x="center")
        elif self.game_state.level > 5:
            arcade.draw_text("VICTORY!", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.GOLD, 50, anchor_x="center")

    def draw_restart_button(self):
        button_width = 220
        button_height = 60
        left = SCREEN_WIDTH / 2 - button_width / 2
        right = SCREEN_WIDTH / 2 + button_width / 2
        top = SCREEN_HEIGHT / 2 + 20
        bottom = top - button_height
        arcade.draw_lrbt_rectangle_filled(left, right, bottom, top, arcade.color.DARK_BLUE)
        arcade.draw_lrbt_rectangle_outline(left, right, bottom, top, arcade.color.WHITE, 3)
        arcade.draw_text("Restart", SCREEN_WIDTH/2, (top + bottom) / 2, arcade.color.WHITE, 24, anchor_x="center", anchor_y="center")

    def on_mouse_press(self, x, y, button, modifiers):
        if self.game_state.game_over:
            button_width = 220
            button_height = 60
            left = SCREEN_WIDTH / 2 - button_width / 2
            right = SCREEN_WIDTH / 2 + button_width / 2
            top = SCREEN_HEIGHT / 2 + 20
            bottom = top - button_height
            if left <= x <= right and bottom <= y <= top:
                self.game_state.reset()
                self.setup()

    def on_update(self, delta_time):
        # 1. Check if we should even be running the rest
        if self.game_state.game_over or self.game_state.level > 5:
            return

        # 2. Normal Game Logic
        prev_bottom = self.player.bottom
        self.player.update()
        self.check_coin_collisions()

        # 3. Void check after update so a falling player can be detected
        if self.player.center_y < 0:
            print(f"DEBUG: Mario is at Y={self.player.center_y}. RESETTING NOW.")
            lost_score = self.coins_collected_this_level * 10
            self.game_state.score = max(0, self.game_state.score - lost_score)
            self.coins_collected_this_level = 0
            self.game_state.lives -= 1
            if self.game_state.lives <= 0:
                self.game_state.game_over = True
                return
            self.setup()
            return # Stop here and restart the frame

        self.enemy_list.update()
        self.check_collisions(prev_bottom)
        
        # CAMERA LOCK
        cx = self.player.center_x
        if cx < SCREEN_WIDTH / 2: cx = SCREEN_WIDTH / 2
        self.camera.position = (cx, SCREEN_HEIGHT / 2)

    def check_collisions(self, prev_bottom):
        if arcade.check_for_collision_with_list(self.player, self.goal_list):
            self.game_state.next_level()
            self.setup()
            return

        # JUMP BUG SHIELD: Aggressive grounding
        hits = arcade.check_for_collision_with_list(self.player, self.platforms)
        if hits and self.player.change_y <= 0:
            valid_hits = [hit for hit in hits if prev_bottom >= hit.top - 5]
            if valid_hits:
                floor_hit = max(valid_hits, key=lambda p: p.top)
                self.player.bottom = floor_hit.top
                self.player.change_y = 0
                self.player.is_on_ground = True
            else:
                self.player.is_on_ground = False
        else:
            # Check for ground 10 pixels below feet
            self.player.bottom -= 10
            is_grounded = arcade.check_for_collision_with_list(self.player, self.platforms)
            self.player.bottom += 10
            self.player.is_on_ground = True if (is_grounded and self.player.change_y <= 0) else False

        # ENEMY COLLISION
        if arcade.check_for_collision_with_list(self.player, self.enemy_list):
            print("MARIO HIT AN ENEMY!")
            lost_score = self.coins_collected_this_level * 10
            self.game_state.score = max(0, self.game_state.score - lost_score)
            self.coins_collected_this_level = 0
            self.game_state.lose_life()
            if not self.game_state.game_over:
                self.setup()

    def check_coin_collisions(self):
        hits = arcade.check_for_collision_with_list(self.player, self.coin_list)
        if hits:
            for coin in hits:
                coin.remove_from_sprite_lists()
                self.coins_collected_this_level += 1
                self.game_state.add_score(10)

    def on_key_press(self, k, m):
        if self.game_state.game_over:
            if k == arcade.key.R:
                self.game_state.reset()
                self.setup()
            elif k == arcade.key.Q:
                self.close()
            return

        if k == arcade.key.UP:
            self.player.jump()
        elif k == arcade.key.LEFT:
            self.player.move_left()
        elif k == arcade.key.RIGHT:
            self.player.move_right()

    def on_key_release(self, k, m):
        if k in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.stop_horizontal()

if __name__ == "__main__":
    window = Mario_Game()
    window.setup()
    arcade.run()