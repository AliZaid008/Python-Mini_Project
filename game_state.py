class GameState:
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.level = 1
        self.game_over = False

    def add_score(self, amount):
        self.score += amount

    def lose_life(self):
        self.lives -= 1
        if self.lives <= 0:
            self.game_over = True
        return self.game_over

    def next_level(self):
        self.level += 1
        if self.level > 5:
            # We can set a victory flag here if we want
            pass

    def reset(self):
        self.score = 0
        self.lives = 3
        self.level = 1
        self.game_over = False
