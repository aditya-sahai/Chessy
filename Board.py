import os
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

    def draw_board(self):
        """Draws the board."""
        self.board_surface.fill((0, 0, 0))
        for row in range(8):
            for col in range(8):
                box_rect = pygame.Rect(
                    col * self.settings.BOX_SIZE,
                    row * self.settings.BOX_SIZE,
                    self.settings.BOX_SIZE,
                    self.settings.BOX_SIZE
                )
                pygame.draw.rect(self.board_surface, self.settings.BOX_COLOUR[(row + col) % 2 == 0], box_rect)
                # observed that sum of row and col at all white boxes is even and odd at black

                square = chess.square(col, 7 - row)
                # subtracted from 7 because numbering of rows in chess starts from the bottom
                piece = self.board.piece_map().get(square)
                if piece:
                    piece_colour = self.settings.PIECE_COLOUR[piece.color]
                    piece_name = chess.piece_name(piece.piece_type)
                    piece_img = self.settings.PIECE_IMGS[piece_colour][piece_name]
                    self.board_surface.blit(piece_img, (box_rect.x, box_rect.y))

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

