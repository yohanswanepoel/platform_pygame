# Game options and settings
WIDTH = 480 #width of the game window
HEIGHT = 600 #height of the game window
FPS = 60 #frames per second that the game runs
TITLE = "Jumper"
# Define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

GRAVITY = 0.5

PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
AIR_FRICTION = -0.02

PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (25, 250, 100, 20),
                 (100, 470, 120, 20),
                 (270, 130, 160, 20),
                 (360, 330, 80, 20),]

