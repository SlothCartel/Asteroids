# Asteroids

This is a simple Asteroids arcade game clone written in Python using Pygame.

## What it is

You control a spaceship and must avoid and shoot asteroids. The game features:
- Player movement and shooting
- Asteroids that split into smaller pieces when shot
- Score and high score tracking
- Game over and restart functionality

## How it works

- The player moves and rotates the ship with WASD keys
- Shoot with the SPACE bar
- Avoid colliding with asteroids
- Destroy asteroids for points; large asteroids split into smaller ones
- The game ends when the player collides with an asteroid
- Press ENTER to restart after game over

## How to run

1. Make sure you have Python 3.12+ installed.
2. Install dependencies (Pygame):
	```bash
	pip install -r requirements.txt
	# or, if using pyproject.toml:
	pip install .
	```
3. Run the game:
	```bash
	python main.py

**Note:**
If you want to change the game's FPS (frames per second), edit the following line in `main.py`:

```python
dt = clock.tick(60) / 1000
```
Change the value `60` to your desired FPS.
	```

Enjoy!
