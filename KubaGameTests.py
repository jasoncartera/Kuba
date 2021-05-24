import unittest
from KubaGame import KubaGame

class TestKubaGame(unittest.TestCase):
    """ Contains tests for KubaGame"""

    def setUp(self) -> None:
        game = KubaGame(('Jason', 'W'), ('Sunny', 'B'))

    def tearDown(self) -> None:
        pass

