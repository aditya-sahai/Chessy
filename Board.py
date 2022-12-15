import io
from cairosvg import svg2png
import pygame
import chess

from PygameConfig import PygameConfig


class Board:
    def __init__(self, settings):
        """Has methods to draw board and update board."""
        self.settings = settings

        self.loop_is_running = True
        self.board_surface = pygame.Surface((self.settings.BOARD_WIDTH, self.settings.BOARD_HEIGHT))

        self.board = chess.Board()
        svg = chess.svg.board(
            self.board,
            fill=dict.fromkeys(self.board.attacks(chess.E4), "#cc0000cc"),
            arrows=[chess.svg.Arrow(chess.E4, chess.F6, color="#0000cccc")],
            squares=chess.SquareSet(chess.BB_DARK_SQUARES & chess.BB_FILE_B),
            size=350,
        )
        self.img = pygame.image.load(svg2png(bytestring=svg))

    def draw_board(self):
        """Draws the board."""
        self.board_surface.fill((0, 0, 0))
        self.board_surface = pygame.image.load(self.img)

    def draw_window(self):
        """Blits the board onto the window and displays the remaining objects."""
        self.settings.win.fill(self.settings.BACKGROUND_COLOUR)
        self.settings.win.blit(self.board_surface, (self.settings.BOARD_X, self.settings.BOARD_Y))
        self.draw_board()

    def main(self):
        """Main game loop."""
        while self.loop_is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.draw_window()
            pygame.display.update()

            self.settings.clock.tick(self.settings.FPS)


if __name__ == "__main__":
    settings = PygameConfig()
    Game = Board(settings)
    Game.main()

