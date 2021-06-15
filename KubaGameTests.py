import unittest
from KubaGame import KubaGame, Player, WhiteMarble, BlackMarble, RedMarble, InvalidName

class TestKubaGame(unittest.TestCase):
    """ Contains tests for KubaGame"""

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def testWinByRedCapture(self):
        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))
        game.make_move('Jason', (5, 6), 'L')
        game.make_move('Sunny', (6, 0), 'R')
        game.make_move('Jason', (5, 5), 'L')
        game.make_move('Sunny', (6, 1), 'R')
        game.make_move('Jason', (5, 4), 'L')
        game.make_move('Sunny', (0, 5), 'B')
        game.make_move('Jason', (5, 3), 'L')
        game.make_move('Sunny', (2, 5), 'L')
        game.make_move('Jason', (5, 2), 'L')
        game.make_move('Sunny', (2, 4), 'L')
        game.make_move('Jason', (5, 0), 'R')
        game.make_move('Sunny', (2, 3), 'L')
        game.make_move('Jason', (5, 1), 'R')
        game.make_move('Sunny', (2, 2), 'L')
        game.make_move('Jason', (6, 6), 'L')
        game.make_move('Sunny', (2, 1), 'L')
        game.make_move('Jason', (6, 5), 'L')
        game.make_move('Sunny', (2, 0), 'F')
        game.make_move('Jason', (6, 3), 'F')
        game.make_move('Sunny', (1, 0), 'F')
        game.make_move('Jason', (5, 3), 'F')
        game.make_move('Sunny', (0, 0), 'B')
        game.make_move('Jason', (4, 3), 'F')
        game.make_move('Sunny', (1, 0), 'B')
        game.make_move('Jason', (3, 3), 'F')
        game.make_move('Sunny', (2, 0), 'B')
        game.make_move('Jason', (2, 3), 'F')
        game.make_move('Sunny', (3, 0), 'R')
        game.make_move('Jason', (6, 4), 'F')
        game.make_move('Sunny', (3, 1), 'R')
        game.make_move('Jason', (5, 4), 'F')
        game.make_move('Sunny', (3, 2), 'R')
        game.make_move('Jason', (4, 4), 'L')
        game.make_move('Sunny', (3, 3), 'R')
        game.make_move('Jason', (4, 3), 'L')
        game.make_move('Sunny', (3, 4), 'R')
        game.make_move('Jason', (4, 2), 'L')
        game.make_move('Sunny', (3, 5), 'R')
        self.assertEqual(game.get_winner(), "Sunny")

    def testMarbleCount(self):
        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))
        game.make_move('Jason', (5, 6), 'L')
        game.make_move('Sunny', (6, 0), 'R')
        game.make_move('Jason', (5, 5), 'L')
        game.make_move('Sunny', (6, 1), 'R')
        game.make_move('Jason', (5, 4), 'L')
        game.make_move('Sunny', (0, 5), 'B')
        game.make_move('Jason', (5, 3), 'L')
        game.make_move('Sunny', (2, 5), 'L')
        game.make_move('Jason', (5, 2), 'L')
        game.make_move('Sunny', (2, 4), 'L')
        game.make_move('Jason', (5, 0), 'R')
        game.make_move('Sunny', (2, 3), 'L')
        game.make_move('Jason', (5, 1), 'R')
        game.make_move('Sunny', (2, 2), 'L')
        game.make_move('Jason', (6, 6), 'L')
        game.make_move('Sunny', (2, 1), 'L')
        game.make_move('Jason', (6, 5), 'L')
        self.assertEqual(game.get_marble_count(), (8,6,9))

    def testPushOffOwn(self):
        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))
        self.assertFalse(game.make_move('Jason', (0,1), 'L'))

    def testNoMovesWin(self):
        board = [[BlackMarble((0,0)), BlackMarble((0,1)), None, None, None, BlackMarble((0,5)), BlackMarble((0,6))],
                       [BlackMarble((1,0)), WhiteMarble((1,1)), RedMarble((1,2)), RedMarble((1,3)), None, BlackMarble((1,5)), BlackMarble((1,6))],
                       [None, RedMarble((2,1)), RedMarble((2,2)), RedMarble((2,3)), RedMarble((2,4)), None, None],
                       [None, RedMarble((3,1)), RedMarble((3,2)), RedMarble((3,3)), RedMarble((3,4)), RedMarble((3,5)), None],
                       [None, None, RedMarble((4,2)), RedMarble((4,3)), RedMarble((4,4)), None, None],
                       [BlackMarble((5,0)), BlackMarble((5,1)), None, RedMarble((5,3)), None, BlackMarble((5,5)), BlackMarble((5,6))],
                       [BlackMarble((6,0)), BlackMarble((6,1)), None, None, None, BlackMarble((6,5)), BlackMarble((6,6))]]

        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'), board)

        self.assertEqual(game.get_winner(), 'Sunny')

    def testInvalidMoveTrapped(self):
        board = [[BlackMarble((0,0)), BlackMarble((0,1)), None, None, None, BlackMarble((0,5)), BlackMarble((0,6))],
                       [BlackMarble((1,0)), WhiteMarble((1,1)), RedMarble((1,2)), RedMarble((1,3)), None, BlackMarble((1,5)), BlackMarble((1,6))],
                       [None, RedMarble((2,1)), RedMarble((2,2)), RedMarble((2,3)), RedMarble((2,4)), None, None],
                       [None, RedMarble((3,1)), RedMarble((3,2)), RedMarble((3,3)), RedMarble((3,4)), RedMarble((3,5)), None],
                       [None, None, RedMarble((4,2)), RedMarble((4,3)), RedMarble((4,4)), None, None],
                       [BlackMarble((5,0)), BlackMarble((5,1)), None, RedMarble((5,3)), None, BlackMarble((5,5)), BlackMarble((5,6))],
                       [BlackMarble((6,0)), BlackMarble((6,1)), None, None, None, WhiteMarble((6,5)), BlackMarble((6,6))]]

        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'), board)
        self.assertFalse(game.make_move('Jason', (1,1), 'F'))

    def testWinByNoMarbles(self):
        board = [[BlackMarble((0,0)), BlackMarble((0,1)), None, None, None, BlackMarble((0,5)), BlackMarble((0,6))],
                       [BlackMarble((1,0)), BlackMarble((1,1)), RedMarble((1,2)), RedMarble((1,3)), None, BlackMarble((1,5)), BlackMarble((1,6))],
                       [None, RedMarble((2,1)), RedMarble((2,2)), RedMarble((2,3)), RedMarble((2,4)), None, None],
                       [None, RedMarble((3,1)), RedMarble((3,2)), RedMarble((3,3)), RedMarble((3,4)), RedMarble((3,5)), None],
                       [None, None, RedMarble((4,2)), BlackMarble((4,3)), RedMarble((4,4)), None, None],
                       [BlackMarble((5,0)), BlackMarble((5,1)), None, RedMarble((5,3)), None, BlackMarble((5,5)), BlackMarble((5,6))],
                       [BlackMarble((6,0)), BlackMarble((6,1)), None, None, None, BlackMarble((6,5)), BlackMarble((6,6))]]

        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'), board)
        self.assertEqual(game.get_winner(), 'Sunny')

    def testGetCurrentTurn(self):
        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))
        game.make_move('Jason', (5, 6), 'L')
        self.assertEqual(game.get_current_turn(), 'Sunny')

    def testGetMarbleBlack(self):
        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))
        self.assertEqual(game.get_marble((0,6)), 'B')

    def testGetMarbleWhite(self):
        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))
        self.assertEqual(game.get_marble((5,5)), 'W')

    def testGetMarbleRed(self):
        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))
        self.assertEqual(game.get_marble((3,3)), 'R')

    def testInvalidName(self):
        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))
        with self.assertRaises(InvalidName):
            game.make_move('Peter', (0, 0), 'R')

    def testKoRuleRight(self):
        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))
        game.make_move('Jason', (5, 6), 'L')
        game.make_move('Sunny', (5, 0), 'R')
        game.make_move('Jason', (5, 5), 'L')
        self.assertEqual(game.ko_rule_move, ((5,0), 'R'))

    def testKoRuleLeft(self):
        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))
        game.make_move('Jason', (1, 0), 'R')
        game.make_move('Sunny', (1, 6), 'L')
        game.make_move('Jason', (1, 1), 'R')
        self.assertEqual(game.ko_rule_move, ((1,6), 'L'))

    def testKoRuleForward(self):
        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))
        game.make_move('Jason', (0, 1), 'B')
        game.make_move('Sunny', (6, 1), 'F')
        game.make_move('Jason', (1, 1), 'B')
        self.assertEqual(game.ko_rule_move, ((6,1), 'F'))

    def testKoRuleBackward(self):
        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))
        game.make_move('Jason', (6, 5), 'F')
        game.make_move('Sunny', (0, 5), 'B')
        game.make_move('Jason', (5, 5), 'F')
        self.assertEqual(game.ko_rule_move, ((0,5), 'B'))

if __name__ == '__main__':
    unittest.main(exit=False)