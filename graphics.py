import pygame
import sys
from pygame.locals import *
from KubaGame import KubaGame, Player
import random

## COLORS ##
GRAY = (176, 179, 184)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Game:
    """
    Main control for KubaGame

    :param playerw is the white marble player
    :param playerb is the black marble player
    """
    def __init__(self, playerw, playerb):
        self._game = KubaGame(playerw, playerb)
        self._playerw = playerw
        self._playerb = playerb
        self._graphics = Graphics()
        self._marble_target = None
        self._marble_dir = None

    @property
    def game(self):
        """
        Game property
        :return: self._game
        """
        return self._game

    @property
    def marble_target(self):
        """
        marble_target property
        :return: self._marble_target
        """
        return self._marble_target

    @marble_target.setter
    def marble_target(self, target):
        self._marble_target = target

    @property
    def marble_dir(self):
        """
        marble direction property
        :return: self._marble_dir
        """
        return self._marble_dir

    @marble_dir.setter
    def marble_dir(self, dir):
        self._marble_dir = dir

    def setup(self):
        """
        Sets up the board game
        """
        self._graphics.set_up_window()
        self._graphics.draw_board_squares()
        self._graphics.draw_marbles(self.game.board.board)

    def game_loop(self):
        """
        Implements the game logic and events triggered and updates the board
        """
        random.seed()
        start = random.randint(0,1)
        if self.game.get_current_turn() is None:
            if start == 0:
                current_player = self._playerw
                self.game.players[self._playerw[0]].is_turn = True
            else:
                current_player = self._playerb
                self.game.players[self._playerb[0]].is_turn = True

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.marble_target = self._graphics.board_coords(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                self.marble_dir = self._graphics.board_coords(pygame.mouse.get_pos())
                if self.game.player_a.is_turn:
                    current_player = self._playerw
                else:
                    current_player = self._playerb

                if self.marble_dir[1] - self.marble_target[1] > 0:
                    self.game.make_move(current_player[0], self.marble_target, 'R')
                elif self.marble_dir[1] - self.marble_target[1] < 0:
                    self.game.make_move(current_player[0], self.marble_target, 'L')
                elif self.marble_dir[0] < self.marble_target[0]:
                    self.game.make_move(current_player[0], self.marble_target, 'F')
                elif self.marble_dir[0] > self.marble_target[0]:
                    self.game.make_move(current_player[0], self.marble_target, 'B')

    def update(self):
        """
        Updates the graphics
        """
        self._graphics.update_display(self.game.board.board, self.game.get_current_turn(), self.game.players[self._playerw[0]].red_captured, self.game.players[self._playerb[0]].red_captured, self.game.get_winner())

    def main(self):
        """
        Executes the game
        """
        self.game_loop()
        self.update()

class Graphics:
    """
    Graphics for the game
    """
    def __init__(self):
        self._width = 602
        self._height = 700
        self._rows = 7
        self._cols = 7
        self._marble_size = self._width // self._cols
        self._caption = "Kuba Game"
        self._screen = pygame.display.set_mode((self._width,self._height))
        self._background = self._screen.fill(GRAY)
        self._playerw_name = None
        self._playerb_name = None
        self._playerb_score = None
        self._playerw_score = None
        self._winner = None

    @property
    def screen(self):
        """
        Screen property
        :return: self._screen
        """
        return self._screen

    @property
    def marble_size(self):
        """
        Marble size property
        :return: self._marble_size
        """
        return self._marble_size

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

    def update_display(self, board, turn, playerw_captured, playerb_captured, winner):
        """
        Updates the display board
        """

        self.screen.fill(GRAY)
        self.draw_board_squares()
        self.draw_marbles(board)
        self.display_status(turn, playerw_captured, playerb_captured, winner)
        pygame.display.update()

    def draw_marbles(self, board):
        """
        Draws the marbles from board object
        """
        for i in range(7):
            for j in range(7):
                if board[i][j] != None:
                    pygame.draw.circle(self._screen, board[i][j].rgb, (j * self._marble_size + self._marble_size / 2, i * self._marble_size + self._marble_size / 2),
                                       self._marble_size / 2.5)

    def board_coords(self, px):
        """
        Converts a tuple of pixel coords to coords on board
        :return square the mouse is on
        """
        row, col = px
        return (col // self._marble_size, row // self._marble_size)


    def display_status(self, turn, playerw_captured, playerb_captured, winner):
        """
        Draws game status to the board
        """
        font_obj = pygame.font.SysFont('arial',20)

        turn_text = font_obj.render(turn + "'s move", True, (0,0,0))
        turn_text_rect = turn_text.get_rect()
        turn_text_rect.move_ip(50, 640)
        self._screen.blit(turn_text, turn_text_rect)

        playerb_text = font_obj.render("Black " + str(playerb_captured) , True, (0,0,0))
        playerb_text_rect = playerb_text.get_rect()
        playerb_text_rect.move_ip(300, 640)
        self._screen.blit(playerb_text, playerb_text_rect)

        playerw_text = font_obj.render("White " + str(playerw_captured) , True, (0,0,0))
        playerw_text_rect = playerw_text.get_rect()
        playerw_text_rect.move_ip(450, 640)
        self._screen.blit(playerw_text, playerw_text_rect)

        if winner:
            win_player = font_obj.render(str(winner) + " Wins!", True, (0, 0, 0))
            win_player_text_rect = win_player.get_rect()
            win_player_text_rect.move_ip(50, 640)
            self._screen.blit(win_player, win_player_text_rect)

def main():
    game = Game(('White', 'W'),('Black', 'B'))
    game.setup()
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        game.main()

if __name__ == '__main__':
    main()