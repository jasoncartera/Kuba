import pygame
from KubaGame import KubaGame, Player

## COLORS ##
GRAY = (176, 179, 184)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Game:
    """
    Main control for KubaGame
    """
    def __init__(self, playera, playerb):
        self._game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))

    @property
    def game(self):
        return self._game

class Graphics:
    """ Graphics for the game """
    def __init__(self):
        self._width = 602
        self._height = 700
        self._rows = 7
        self._cols = 7
        self._marble_size = self._width // self._cols
        self._caption = "Kuba Game"
        self._screen = pygame.display.set_mode((self._width,self._height))
        self._background = self._screen.fill(GRAY)

    def set_up_window(self):
        """
        Initializes the game window
        """
        pygame.init()
        pygame.display.set_caption(self._caption)

    def draw_board_squares(self):
        """
        Takes a board object and draws the squares to the display
        """
        for x in range(0, 602, 86):
            for y in range(0, 602, 86):
                rect = pygame.Rect(x, y, 86, 86)
                pygame.draw.rect(self._screen, BLACK, rect, 1)

    def update_display(self, board):
        """
        Updates the display board
        """
        self.draw_board_squares()
        self.draw_marbles(board)
        pygame.display.update()

    def draw_marbles(self, board):
        """
        Draws the marbles from board object
        """
        # TODO position marbles in each square from the game.game.board

def main():
    graphic = Graphics()
    game = Game(('Jason', 'W'),('Sunny', 'B'))
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        graphic.update_display(game.game.board)

    pygame.quit()

if __name__ == '__main__':
    main()