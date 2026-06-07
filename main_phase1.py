import arcade
from mario_game import Mario_Game

def main():
    window = Mario_Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()