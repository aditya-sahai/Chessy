import os
import pygame
import chess


class PygameConfig:
    def __init__(self):
        # Dimensions and window
        self.BOX_SIZE = 75
        self.WIDTH = self.BOX_SIZE * 9
        self.HEIGHT = self.BOX_SIZE * 9
        self.BOARD_WIDTH = self.BOX_SIZE * 8
        self.BOARD_HEIGHT = self.BOX_SIZE * 8

        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Chessy")

        # Positions
        self.BOARD_X = self.BOX_SIZE // 2
        self.BOARD_Y = self.BOX_SIZE // 2

        # Clock
        self.FPS = 60
        self.clock = pygame.time.Clock()

        # Board colour settings
        self.BACKGROUND_COLOUR = (207, 207, 207)
        self.WHITE_COLOUR = (237, 237, 237)
        self.BLACK_COLOUR = (100, 160, 100)

        # path
        self.BASE_DIR = os.getcwd()

        # game related variables
        self.BOX_COLOUR = {True: self.WHITE_COLOUR, False: self.BLACK_COLOUR}
        self.PIECE_COLOUR = {True: "white", False: "black"}

        self.load_piece_images()

    def load_piece_images(self):
        """
        Loads the piece images into a dictionary so that they can be rendered.
        """
        self.PIECE_IMGS = {"white": {}, "black": {}}
        for piece_type in range(1, 7):
            piece_name = chess.piece_name(piece_type)
            self.PIECE_IMGS["white"][piece_name] = pygame.image.load(
                os.path.join(self.BASE_DIR, f"images\pieces\white\{piece_name}.png")
            ).convert_alpha()
            self.PIECE_IMGS["black"][piece_name] = pygame.image.load(
                os.path.join(self.BASE_DIR, f"images\pieces\\black\{piece_name}.png")
            ).convert_alpha()