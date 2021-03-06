# Author: Jason Carter
# Date: 5/29/2021
# Description: Implementation of the Kuba game.

import copy

class Player:
    """ Represents a player. This class contains the player name, color, how many marbles are left, turn status, and how many red marbles are captured.
        The Player class is also responsible for determining what moves are available for a player given a board state
        This class must communicate with the KubaGame class in order to receive two parameters for the available_moves method and return
        the available moves for the player.
    """

    def __init__(self, name, color):
        """
        Initializes a player with name and color.

        Attributes:
            name: Player's name
            color: Player's marble color
            is_turn: None if the game hasn't started and a bool if the game has started.
            red_captured: the number of red marbles captured by the player.
            marbles_left: Number of marbles the player has left

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
        """ The player name property
            :return self._name
        """
        return self._name

    @property
    def color(self):
        """ Player marble color property
            :return self_color
        """
        return self._color

    @property
    def is_turn(self):
        """ Player turn property as bool
            :return self._is_turn
        """
        return self._is_turn

    @is_turn.setter
    def is_turn(self, turn):
        """ Is turn setter """
        self._is_turn = turn

    @property
    def marbles_left(self):
        """ Marbles left property
            :return self._marbles_left
        """
        return self._marbles_left

    @property
    def red_captured(self):
        """ Number of captured red marbles property
            :return self._red_captured
        """
        return self._red_captured

    def update_marbles_left(self):
        """ Subtracts one from the total number or marbles on the board """
        self._marbles_left -= 1

    def update_red_captured(self):
        """ Updates the number of captured red marbles by one """
        self._red_captured += 1

    def available_moves(self, board, ko_rule):
        """
        Determines moves a player has available
        :param board: KubaGame.Board
        :ko_rule: the current Ko Rule
        :return: list of valid moves as tuple (row, col)
        """

        board = board.board
        available_moves = list()
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] is not None and board[row][col].color == self.color:
                    if row < 6:
                        if board[row + 1][col] is None:
                            available_moves.append(((row, col), 'F'))
                    if row > 0:
                        if board[row - 1][col] is None:
                            available_moves.append(((row, col), 'B'))
                    if col < 6:
                        if board[row][col + 1] is None:
                            available_moves.append(((row, col), 'L'))
                    if col > 0:
                        if board[row][col - 1] is None:
                            available_moves.append(((row, col), 'R'))
                    if col == 6:
                        available_moves.append(((row, col), 'L'))
                    if row == 6:
                        available_moves.append(((row, col), 'F'))
                    if col == 0:
                        available_moves.append(((row, col), 'R'))
                    if row == 0:
                        available_moves.append(((row, col), 'B'))

        if ko_rule in available_moves:
            available_moves.remove(ko_rule)

        return available_moves

class Marble:
    """ Represents a marble. Communicates with the KubaGame class to determine color.

        Attributes:
            pos: the position of the marble (row, col) as a tuple
    """

    def __init__(self, pos):
        """
        A marble
        :param pos: current position of the marble on the board
        """
        self._pos = pos

    @property
    def pos(self):
        """ Pos property
            :return self._pos
        """
        return self._pos

    @pos.setter
    def pos(self, new_pos):
        """ Pos setter """
        self._pos = new_pos

class WhiteMarble(Marble):
    """ A white marble inherits from Marble

        Attributes:
            color: the color of the marble
    """

    def __init__(self, pos):
        """ Inits a white marble """
        super().__init__(pos)
        self._color = 'W'
        self._rgb = (255, 255, 255)

    @property
    def color(self):
        """ Color property
            :return self._color
        """
        return self._color

    @property
    def rgb(self):
        """ RGB property
        :return self._rgb
        """
        return self._rgb

class BlackMarble(Marble):
    """ A black marble inherits from Marble

        Attributes:
            color: the color of the marble
    """

    def __init__(self, pos):
        """ Inits a black marble """
        super().__init__(pos)
        self._color = 'B'
        self._rgb = (0, 0, 0)

    @property
    def color(self):
        return self._color

    @property
    def rgb(self):
        """ RGB property
        :return self._rgb
        """
        return self._rgb

class RedMarble(Marble):
    """ A red marble inherits from Marble

        Attributes:
            color: the color of the marble
    """

    def __init__(self, pos):
        """ Inits a red marble """
        super().__init__(pos)
        self._color = 'R'
        self._rgb = (255, 0, 0)

    @property
    def color(self):
        return self._color

    @property
    def rgb(self):
        """ RGB property
        :return self._rgb
        """
        return self._rgb

class Board:
    """ Represents a Kuba board.

        Attributes:
            board: 2D array representation of a 7x7 game board
    """

    def __init__(self, board=None):
        """ Initializes a board with marbles in the correct starting location

            :param board: optional 2D array starting board. Should be used for testing board conditions
        """
        if board is None:
            self._board = [
                [WhiteMarble((0, 0)), WhiteMarble((0, 1)), None, None, None, BlackMarble((0, 5)), BlackMarble((0, 6))],
                [WhiteMarble((1, 0)), WhiteMarble((1, 1)), None, RedMarble((1, 3)), None, BlackMarble((1, 5)), BlackMarble((1, 6))],
                [None, None, RedMarble((2, 2)), RedMarble((2, 3)), RedMarble((2, 4)), None, None],
                [None, RedMarble((3, 1)), RedMarble((3, 2)), RedMarble((3, 3)), RedMarble((3, 4)), RedMarble((3, 5)), None],
                [None, None, RedMarble((4, 2)), RedMarble((4, 3)), RedMarble((4, 4)), None, None],
                [BlackMarble((5, 0)), BlackMarble((5, 1)), None, RedMarble((5, 3)), None, WhiteMarble((5, 5)), WhiteMarble((5, 6))],
                [BlackMarble((6, 0)), BlackMarble((6, 1)), None, None, None, WhiteMarble((6, 5)), WhiteMarble((6, 6))]]
        else:
            self._board = board

    @property
    def board(self):
        """ The board property
            :return self._board
        """
        return self._board

    @board.setter
    def board(self, update_board):
        """ The board setter """
        self._board = update_board

    def update_board(self, coord, dir):
        """
        Updates the board based on a given coordinate and direction.

        :param coord: coordinate on the board that is being played
        :param dir: direction the coordinate will be 'pushed'
        :return: pushed_off - None or the marble pushed off the board
        """

        pushed_off = None

        if dir == 'R':
            # To iterate through column
            col = coord[1]
            marbles = []
            # Create a list of the marbles in the chain being pushed
            while col < len(self.board[0]) and self.board[coord[0]][col] is not None:
                marbles.append(self.board[coord[0]][col])
                col += 1

            # Update position of marbles and pop final marble in marbles since it will be pushed off if already at
            # the board edge
            for marble in marbles:
                if marble.pos[1] == 6:
                    pushed_off = marbles.pop()
                else:
                    marble.pos = marble.pos[0], marble.pos[1] + 1

            # Update the board with new marble positions
            for marble in marbles:
                self.board[coord[0]][marble.pos[1]] = marble

            # Set the pushed space to None
            self.board[coord[0]][coord[1]] = None
            return pushed_off

        if dir == 'L':
            col = coord[1]
            marbles = []
            while col >= 0 and self.board[coord[0]][col] is not None:
                marbles.append(self.board[coord[0]][col])
                col -= 1
            for marble in marbles:
                if marble.pos[1] == 0:
                    pushed_off = marbles.pop()
                else:
                    marble.pos = marble.pos[0], marble.pos[1] - 1

            for marble in marbles:
                self.board[coord[0]][marble.pos[1]] = marble

            self.board[coord[0]][coord[1]] = None
            return pushed_off

        if dir == 'B':
            row = coord[0]
            marbles = []
            while row < len(self.board[0]) and self.board[row][coord[1]] is not None:
                marbles.append(self.board[row][coord[1]])
                row += 1

            for marble in marbles:
                if marble.pos[0] == 6:
                    pushed_off = marbles.pop()
                else:
                    marble.pos = marble.pos[0] + 1, marble.pos[1]

            for marble in marbles:
                self.board[marble.pos[0]][coord[1]] = marble

            self.board[coord[0]][coord[1]] = None
            return pushed_off

        if dir == 'F':
            row = coord[0]
            marbles = []
            while row >= 0 and self.board[row][coord[1]] is not None:
                marbles.append(self.board[row][coord[1]])
                row -= 1
            for marble in marbles:
                if marble.pos[0] == 0:
                    pushed_off = marbles.pop()
                else:
                    marble.pos = marble.pos[0] - 1, marble.pos[1]

            for marble in marbles:
                self.board[marble.pos[0]][coord[1]] = marble

            self.board[coord[0]][coord[1]] = None
            return pushed_off

    def print_board(self):
        """ Prints the current state of the board as text """

        for i in self.board:
            for j in i:
                if j is None:
                    print('X', end=' ')
                else:
                    print(j.color, end=' ', )
            print()


class KubaGame:
    """ Class represents the game of Kuba

        Attributes:
            player_a: player a
            player_b player b
            board: optional parameter to initialize the board for testing
            players: dictionary of the two players with the player name as a key
            ko_rule_move: the move that would return the game to the previous state
    """

    def __init__(self, player_a, player_b, board=None):
        """
        Initializes the Kuba game with two players and the player marble color.
        Initializes the game board.
        Initializes two players
        This class communicates with the Board class, the Player class, and the Marble classes

        :param player_a: tuple (player name, marble color)
        :param player_b: tuple (player name, marble color)
        :param board: Optional 2D array starting board

        ko_rule_move keeps track of which move is invalid per the Ko Rule
        """

        self._player_a = Player(player_a[0], player_a[1])
        self._player_b = Player(player_b[0], player_b[1])
        self._players = {player_a[0]: self._player_a, player_b[0]: self._player_b}
        if board == None:
            self._board = Board()
        else:
            self._board = Board(board)
        self._ko_rule_move = None

    @property
    def board(self):
        """ Board property
            :return self._board
        """
        return self._board

    @property
    def player_a(self):
        """ Player_a property
            :return self._player_a
        """
        return self._player_a

    @property
    def player_b(self):
        """ Player_b property
            :return self._player_b
        """
        return self._player_b

    @property
    def players(self):
        """ Players property
            :return self._players
        """
        return self._players

    @property
    def ko_rule_move(self):
        """ Ko rule property
            :return self._ko_rule_move
        """
        return self._ko_rule_move

    @ko_rule_move.setter
    def ko_rule_move(self, move):
        """ Sets the ko rule """
        self._ko_rule_move = move

    def get_current_turn(self):
        """
        Gets the name of the player who's turn it is.
        :return: Player name or None
        """

        if self.player_a.is_turn is None and self.player_b.is_turn is None:
            return None
        elif self.player_a.is_turn:
            return self.player_a.name
        elif self.player_b.is_turn:
            return self.player_b.name

    def make_move(self, player, coord, dir):
        """
        Makes a move on the board.

        :param player: Name of the player to make the move
        :param coord: Coordinates of the marble that is going to be moved.
        :param dir: Direction that the marble will be moved. Valid directions are Left (L), Right (R), Backward (B), and Forward (F)
        :return: True if move is successful, False if not
        """

        if not self.players.get(player):
            raise InvalidName

        # If this is the first move establish player turns
        if self.get_current_turn() is None:
            if player == self.player_a.name:
                self.player_a.is_turn = True
                self.player_b.is_turn = False
            else:
                self.player_b.is_turn = True
                self.player_a.is_turn = False

        ko_temp = self.ko_rule_move

        move = ((coord), dir)
        # If there is a winner
        if self.get_winner():
            return False
        # If move is not available
        if move not in self.players[player].available_moves(self.board, self.ko_rule_move):
            return False
        # If coord out of bounds
        if coord[0] > 6 or coord[1] > 6 or coord[0] < 0 or coord[1] < 0:
            return False
        # If the coord is an empty square
        if self.board.board[coord[0]][coord[1]] is None:
            return False
        # If it is not the players turn
        if player != self.get_current_turn():
            return False

        # If we made it here, update the ko rule move
        self.update_ko_rule((coord, dir))

        previous_board = copy.deepcopy(self.board.board)

        # Make the move and save captured marble in captured_marble (Marble object or None)
        captured_marble = self.board.update_board(coord, dir)

        # If player captured their own marble, revert board back to before the move was made and return False
        if captured_marble is not None and captured_marble.color == self.players[player].color:
            self.board.board = previous_board
            self.ko_rule_move = ko_temp
            return False

        # Update marble counts
        if captured_marble is not None and captured_marble.color == 'R':
            self.players[player].update_red_captured()
        if self.player_a.is_turn and captured_marble is not None and captured_marble.color == self.player_b.color:
            self.player_b.update_marbles_left()
        if self.player_b.is_turn and captured_marble is not None and captured_marble.color == self.player_a.color:
            self.player_a.update_marbles_left()

        # Update player turns after making the move
        if player == self.player_a.name:
            self.player_a.is_turn = False
            self.player_b.is_turn = True
        else:
            self.player_a.is_turn = True
            self.player_b.is_turn = False

        return True

    def update_ko_rule(self, move):
        """
        Determines what move is forbidden per the Ko rule. Calculated before the move in make_move is made.

        :param move: coordinates of move and the direction from make_move
        :return: self.ko_rule_move
        """

        if move[1] == 'R':
            # To iterate through column
            col = move[0][1]
            # Before making the move in make_move, determine when the row or col is None. This is were the marble row
            # or column will terminate after the move is made.
            try:
                while self.board.board[move[0][0]][col] is not None:
                    col += 1
                self.ko_rule_move = ((move[0][0], col), 'L')
                return self.ko_rule_move
            # If move will result in marble dropping off, Ko rule doesn't apply
            except IndexError:
                self.ko_rule_move = None
                return self.ko_rule_move

        if move[1] == 'L':
            col = move[0][1]
            try:
                while self.board.board[move[0][0]][col] is not None:
                    col -= 1
                self.ko_rule_move = ((move[0][0], col), 'R')
                return self.ko_rule_move
            except IndexError:
                self.ko_rule_move = None
                return self.ko_rule_move

        if move[1] == 'B':
            row = move[0][0]
            try:
                while self.board.board[row][move[0][1]] is not None:
                    row += 1
                self.ko_rule_move = ((row, move[0][1]), 'F')
                return self.ko_rule_move
            except IndexError:
                self.ko_rule_move = None
                return self.ko_rule_move

        if move[1] == 'F':
            row = move[0][0]
            try:
                while self.board.board[row][move[0][1]] is not None:
                    row -= 1
                self.ko_rule_move = ((row, move[0][1]), 'B')
                return self.ko_rule_move
            except IndexError:
                self.ko_rule_move = None
                return self.ko_rule_move

    def get_winner(self):
        """
        Determines if there is a winner.

        :return: returns the name of the winning player. If no winner, returns None
        """

        if self.player_a.red_captured == 7:
            return self.player_a.name
        elif self.player_b.red_captured == 7:
            return self.player_b.name
        elif self.player_a.marbles_left == 0 and self.player_b.marbles_left > 0:
            return self.player_b.name
        elif self.player_b.marbles_left == 0 and self.player_a.marbles_left > 0:
            return self.player_a.name
        elif len(self.player_a.available_moves(self.board, self.ko_rule_move)) == 0:
            return self.player_b.name
        elif len(self.player_b.available_moves(self.board, self.ko_rule_move)) == 0:
            return self.player_a.name
        else:
            return None

    def get_captured(self, player):
        """
        Returns how many red marbles a given player has captured

        :param player: name of a player
        :return: How many Red marbles the given player has captured
        """

        try:
            return self.players[player].red_captured
        except KeyError:
            raise InvalidName

    def get_marble(self, coords):
        """
        Gets the marble type at a given coordinate

        :param coords: Coordinates of a cell on the board
        :return: The color of marble at the coordinate or X if no marble is located at the coord.
        """

        if self.board.board[coords[0]][coords[1]] is None:
            return 'X'
        else:
            return self.board.board[coords[0]][coords[1]].color

    def get_marble_count(self):
        """
        Gets the total marble count on the board

        :return: The number of white, black, and red marbles on the board as a tuple in (W, B, R) order
        """

        if self.player_a.color == 'W':
            player_white = self.player_a
            player_black = self.player_b
        else:
            player_black = self.player_a
            player_white = self.player_b

        return (player_white.marbles_left, player_black.marbles_left,
                13 - player_black.red_captured - player_white.red_captured)

class InvalidName(Exception):
    """ Raised if an invalid player name is used"""
    pass

