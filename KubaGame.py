# Author: Jason Carter
# Date: 5/22/2021
# Description: Implementation of the Kuba game.

class Player:
    """ Represents a player"""

    def __init__(self, name, color):
        """
        Initializes a player with name and color. _is_turn is None if the game hasn't started and a bool if the game has started.
        red_captured is the number of red marbles captured by the player.

        :param name: Player name
        :param color: Player color
        """
        self._name = name
        self._color = color
        self._is_turn = None
        self._red_captured = 0
        self._marbles_left = 8

    @property
    def name(self):
        """ The player name property"""
        return self._name

    @property
    def color(self):
        """ Player marble color property"""
        return self._color

    @property
    def is_turn(self):
        """ Player turn property as bool"""
        return self._is_turn

    @is_turn.setter
    def is_turn(self, turn):
        """ Is turn setter"""
        self._is_turn = turn

    @property
    def marbles_left(self):
        """ Marbles left property"""
        return self._marbles_left

    def update_marbles_left(self):
        """ Subtracts one from the total number or marbles on the board"""
        self._marbles_left -= 1

    @property
    def red_captured(self):
        """ Number of captured red marbles property"""
        return self._red_captured

    def update_red_captured(self):
        """ Updates the number of captured red marbles by one"""
        self.red_captured += 1


class Board:
    """ Represents a Kuba board"""

    def __init__(self):
        """ Initializes a board with marbles in the correct starting location"""
        self._board = [['W', 'W', None, None, None, 'B', 'B'],
                       ['W', 'W', None, 'R', None, 'B', 'B'],
                       [None, None, 'R', 'R', 'R', None, None],
                       [None, 'R', 'R', 'R', 'R', 'R', None],
                       [None, None, 'R', 'R', 'R', None, None],
                       ['B', 'B', None, 'R', None, 'W', 'W'],
                       ['B', 'B', None, None, None, 'W', 'W']]

    @property
    def board(self):
        """ The board property"""
        return self._board

    def print_board(self):
        """ Prints the current state of the board"""

        for i in self.board:
            for j in i:
                if j is None:
                    print('X', end=' ')
                else:
                    print(j, end=' ',)
            print()

class KubaGame:
    """ Class represents the game of Kuba"""

    def __init__(self, player_a, player_b):
        """
        Initializes the Kuba game with two players and the player marble color. Initializes the game
        board.

        :param player_a: tuple (player name, marble color)
        :param player_b: tuple (player name, marble color)
        """

        self._player_a = Player(player_a[0], player_a[1])
        self._player_b = Player(player_b[0], player_a[1])
        self._board = Board()

    @property
    def board(self):
        """ Board property"""
        return self._board

    @property
    def player_a(self):
        """ Player_a property"""
        return self._player_a

    @property
    def player_b(self):
        """Player_b property"""
        return self._player_b

    def get_current_turn(self):
        """
        Gets the name of the player who's turn it is. Returns none if no player has moved.
        :return: Player name or None
        """

        if self.player_a.is_turn is None and self.player_b.is_turn is None:
            return None
        elif self.player_a.is_turn:
            return self.player_a.name
        elif self.player_b.is_turn:
            return self.player_b.name

    def make_move(self, player, coords, dir):
        """
        Makes a move on the board.

        :param player: Name of the player to make the move
        :param coords: Coordinates of the marble that is going to be moved.
        :param dir: Direction that the marble will be moved. Valid directions are Left (L), Right (R), Backward (B), and Forward (F)
        :return: True if move is successful, False if not
        """

        pass

    def get_winner(self):
        """

        :return: returns the name of the winning player. If no winner, returns None
        """
        if self.player_a.red_captured == 7:
            return self.player_a.name
        elif self.player_b.red_captured == 7:
            return self.player_b.name
        elif self.player_a.marbles_left == 0 and self.player_b.marbles_left > 0:
            return self.player_b
        elif self.player_b.marbles_left == 0 and self.player_a.marbles_left > 0:
            return self.player_a
        else:
            return None

    def get_captured(self, player):
        """

        :param player: name of a player
        :return: How many Red marbles the given player has captured
        """
        if self.player_a.name == player:
            return self.player_a.red_captured
        elif self.player_b.name == player:
            return self.player_b.red_captured
        else:
            raise InvalidName

    def get_marble(self, coords):
        """

        :param coords: Coordinates of a cell on the board
        :return: The color of marble at the coordinate or X if no marble is located at the coord.
        """

        if self.board[coords[0]][coords[1]] is None:
            return 'X'
        else:
            return self.board[coords[0]][coords[1]]

    def get_marble_count(self):
        """

        :return: THe number of white, black, and red marbles on the board as a tuple in (W, B, R) order
        """

        if self.player_a.color == 'W':
            player_white = self.player_a
            player_black = self.player_b
        else:
            player_black = self.player_a
            player_white = self.player_b

        return (player_white.marbles_left, player_black.marbles_left, 13-player_black.red_captured-player_white.red_captured)

class InvalidName(Exception):
    """ Raised if an invalid player name is used"""
    pass

def main():
    game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))
    print(game.get_marble_count())
if __name__ == '__main__':
    main()
