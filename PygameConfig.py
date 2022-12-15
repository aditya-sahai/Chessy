import pygame


class PygameConfig:
    def __init__(self):
        # Dimensions and window
        self.BOX_SIZE = 75
        self.WIDTH = self.BOX_SIZE * 9
        self.HEIGHT = self.BOX_SIZE * 9
        self.BOARD_WIDTH = self.BOX_SIZE * 8
        self.BOARD_HEIGHT = self.BOX_SIZE * 8

        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Positions
        self.BOARD_X = self.BOX_SIZE // 2
        self.BOARD_Y = self.BOX_SIZE // 2

        # Clock
        self.FPS = 60
        self.clock = pygame.time.Clock()

        # Board colour settings
        self.BACKGROUND_COLOUR = (207, 207, 207)
        self.WHITE_COLOUR = (237, 237, 237)
        self.BLACK_COLOUR = (116, 176, 117)