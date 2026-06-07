# Retro Platformer (Arcade)

A classic 2D side-scrolling platformer built entirely in Python using the **Arcade** library. Navigate through 5 unique, progressively difficult stages, dodge moving enemies, and master tricky jumps to reach the victory flag.

## 🚀 Features

* **5 Unique Levels:** Hand-crafted platforming challenges that grow more difficult with every level cleared.
* **Custom Physics Shield:** Features a robust ground-detection system ("Coyote Time" buffering) to completely eliminate the common platformer "jump bug."
* **Horizontal Camera Tracking:** The game camera smoothly follows the player dynamically across the horizontal plane while keeping vertical bounds tightly locked.
* **Instant Void Reset:** Custom falling math guarantees that dropping below the level boundaries registers immediately and flawlessly resets the stage.
* **State Management:** Track lives, scores, and active level progressions dynamically across scenes.

## 🕹️ Controls

* `Left Arrow` – Move Left
* `Right Arrow` – Move Right
* `Up Arrow` – Jump

## 🛠️ Project Structure

* `main_phase1.py` — The primary launcher and execution file.
* `mario_game.py` — Core window logic, level building, frame rendering, and collision handling.
* `player.py` — Handle player mechanics, vector movement, and jump velocities.
* `enemy.py` — Logic for patrol boundaries and horizontal pathing enemies.
* `game_state.py` — Global tracker for current levels, remaining lives, and win/loss states.
* `constants.py` — Centralized global configs (screen bounds, gravity parameters).

## 📦 Installation & Setup

1. Make sure you have **Python 3.10+** installed on your machine.
2. Clone this repository to your local directory:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
