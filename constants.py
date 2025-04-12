import os

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_SPLIT_SPEED_UP_FACTOR = 1.2

OBJECT_DRAW_WIDTH = 4

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3

SHOT_RADIUS = 5

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKGROUNDS = ["llamas", "capybaras"]
OBJECT_COLOR = "black"