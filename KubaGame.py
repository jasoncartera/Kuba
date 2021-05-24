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
        self._red_captured += 1

    def available_moves(self, board):
        """
        Determines moves a player has avalaible
        :param board: KubaGame.Board
        :return: set of valid moves as tuple (row, col)
        """
        board = board.board
        available_moves = set()

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == self.color:
                    if row < 6:
                        if board[row+1][col] is None:
                            available_moves.add((row, col))
                    if row > 0:
                        if board[row-1][col] is None:
                            available_moves.add((row, col))
                    if col < 6:
                        if board[row][col+1] is None:
                            available_moves.add((row, col))
                    if col > 0:
                        if board[row][col-1] is None:
                            available_moves.add((row, col))

        return available_moves

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

    @board.setter
    def board(self, update_board):
        self._board = update_board

    def update_board(self, coord, dir):
        """
        Updates the board based on a given coordinate and direction
        :param coord: coordinate on the board that is being played
        :param dir: direction the coordinate will be 'pushed'
        :return: Marble no longer in a given row or column if one was pushed off
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

            if col > len(self.board[0])-1:
                pushed_off = marbles.pop()
                col -= 1

            for marble in marbles[::-1]:
                self.board[coord[0]][col] = marble
                col -= 1

            self.board[coord[0]][coord[1]] = None
            return pushed_off

        if dir == 'L':
            # To iterate through column
            col = coord[1]
            marbles = []
            # Create a list of the marbles in the chain being pushed
            while col >= 0 and self.board[coord[0]][col] is not None:
                marbles.append(self.board[coord[0]][col])
                col -= 1

            if col < 0:
                pushed_off = marbles.pop()
                col += 1

            for marble in marbles[::-1]:
                self.board[coord[0]][col] = marble
                col += 1

            self.board[coord[0]][coord[1]] = None
            return pushed_off

        if dir == 'B':
            # To iterate through column
            row = coord[0]
            col_before = []
            for i in range(len(self.board[0])):
                col_before.append(self.board[i][coord[1]])

            marbles = []
            # Create a list of the marbles in the chain being pushed
            while row < len(self.board[0]) and self.board[row][coord[1]] is not None:
                marbles.append(self.board[row][coord[1]])
                row += 1

            if row > len(self.board[0])-1:
                pushed_off = marbles.pop()
                row -= 1

            for marble in marbles[::-1]:
                self.board[row][coord[1]] = marble
                row -= 1

            self.board[coord[0]][coord[1]] = None
            return pushed_off

        if dir == 'F':
            # To iterate through column
            row = coord[0]
            marbles = []
            # Create a list of the marbles in the chain being pushed
            while row >= 0 and self.board[row][coord[1]] is not None:
                marbles.append(self.board[row][coord[1]])
                row -= 1

            if row < 0:
                pushed_off = marbles.pop()
                row += 1

            for marble in marbles[::-1]:
                self.board[row][coord[1]] = marble
                row += 1

            self.board[coord[0]][coord[1]] = None
            return pushed_off

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

        ko_rule_move keeps track of which move is invalid per the Ko Rule
        """

        self._player_a = Player(player_a[0], player_a[1])
        self._player_b = Player(player_b[0], player_b[1])
        self._players = {player_a[0]: self._player_a, player_b[0]: self._player_b}
        self._board = Board()
        self._ko_rule_move = None

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

    @property
    def players(self):
        """Players property"""
        return self._players

    @property
    def ko_rule_move(self):
        """ Ko rule property"""
        return self._ko_rule_move

    @ko_rule_move.setter
    def ko_rule_move(self, move):
        self._ko_rule_move = move

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

    def make_move(self, player, coord, dir):
        """
        Makes a move on the board.

        :param player: Name of the player to make the move
        :param coord: Coordinates of the marble that is going to be moved.
        :param dir: Direction that the marble will be moved. Valid directions are Left (L), Right (R), Backward (B), and Forward (F)
        :return: True if move is successful, False if not
        """

        # If this is the first move establish player turns
        if self.get_current_turn() is None:
            if player == self.player_a.name:
                self.player_a.is_turn = True
                self.player_b.is_turn = False
            else:
                self.player_b.is_turn = True
                self.player_a.is_turn = False

        # If there is a winner
        if self.get_winner():
            return False
        # If coord out of bounds
        if coord[0] > 6 or coord[1] > 6:
            return False
        # If it is not the players turn
        if player != self.get_current_turn():
            return False
        # If dir is not valid
        if dir not in self.valid_move_dir(coord):
            return False
        # If move would be the opposite of last move return false
        if (coord, dir) == self.ko_rule_move:
            return False
        # Need to account for if player is pushing the wrong color
        if self.board.board[coord[0]][coord[1]] != self.players[player].color:
            return False

        # Temporary board copy to revert board to previous state if pushing off players own piece
        previous_board = [x[:] for x in self.board.board]

        # If we made it here, update the ko rule move and make the move
        self.update_ko_rule((coord, dir))

        # Make the move - Need to update captures and marble losses
        captured_marble = self.board.update_board(coord, dir)

        # If player captured their own marble, revert board back to before the move was made and return False
        if captured_marble == self.players[player].color:
            self.board.board = previous_board
            return False

        # Update marble counts
        if captured_marble == 'R':
            self.players[player].update_red_captured()
        if self.player_a.is_turn and captured_marble == self.player_b.color:
            self.player_b.update_marbles_left()
        if self.player_b.is_turn and captured_marble == self.player_a.color:
            self.player_a.update_marbles_left()

        # Update player turns after making the move
        if player == self.player_a.name:
            self.player_a.is_turn = False
            self.player_b.is_turn = True
        else:
            self.player_a.is_turn = True
            self.player_b.is_turn = False

        return True

    def valid_move_dir(self, coord):
        """
        Returns a set of valid move directions for a coordinate
        :param coords: Coordinate of proposed move
        :return: set of valid directions to move
        """

        valid_dir = set()
        r,c = coord
        if c == 0:
            valid_dir.add('R')
        if c == 6:
            valid_dir.add('L')
        if r == 0:
            valid_dir.add('B')
        if r == 6:
            valid_dir.add('F')
        if r-1 >= 0 and self.board.board[r-1][c] is None:
            valid_dir.add('B')
        if r+1 <= 6 and self.board.board[r+1][c] is None:
            valid_dir.add('F')
        if c-1 >= 0 and self.board.board[r][c-1] is None:
            valid_dir.add('R')
        if c+1 <= 6 and self.board.board[r][c+1] is None:
            valid_dir.add('L')

        return valid_dir

    def update_ko_rule(self, move):
        """
        Determines what move is forbidden per the Ko rule. Calculated before the move in make_move is made
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
        elif len(self.player_a.available_moves(self.board)) == 0:
            return self.player_b.name
        elif len(self.player_b.available_moves(self.board)) == 0:
            return self.player_a.name
        else:
            return None



    def get_captured(self, player):
        """

        :param player: name of a player
        :return: How many Red marbles the given player has captured
        """
        try:
            return self.players[player].red_captured
        except KeyError:
            raise InvalidName

    def get_marble(self, coords):
        """

        :param coords: Coordinates of a cell on the board
        :return: The color of marble at the coordinate or X if no marble is located at the coord.
        """

        if self.board.board[coords[0]][coords[1]] is None:
            return 'X'
        else:
            return self.board.board[coords[0]][coords[1]]

    def get_marble_count(self):
        """

        :return: The number of white, black, and red marbles on the board as a tuple in (W, B, R) order
        """

        if self.player_a.color == 'W':
            player_white = self.player_a
            player_black = self.player_b
        else:
            player_black = self.player_a
            player_white = self.player_b

        # Calculates the number of marbles left based on how many marbles each player has.
        # Since the Board class doesn't care about how many marbles there are, I thought it was more
        # appropriate to have the Player class keep track of this.
        return (player_white.marbles_left, player_black.marbles_left, 13-player_black.red_captured-player_white.red_captured)


class InvalidName(Exception):
    """ Raised if an invalid player name is used"""
    pass

if __name__ == '__main__':
    game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))
    game.get_marble_count()
    game.board.print_board()
    print("Jason red: ", game.get_captured('Jason'))
    print("Sunny red: ", game.get_captured('Sunny'))
    print("Winner: ", game.get_winner())
    print(game.get_marble_count())
