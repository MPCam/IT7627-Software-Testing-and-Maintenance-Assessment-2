"""
Unit tests for class BowlingGame

Test have been put into the class TestsBowlingGame

These tests demonstrate the required outcomes of each function,
the tests are:
1. Test random score
2. Test rolls
3. Test current roll
4. Test strike and bonus
5. Test spare and bonus
6. Test frame one
7. Test frame ten
"""
from bowling_game import BowlingGame
import unittest


class TestsBowlingGame(unittest.TestCase):

    def setUp(self):
        """
        Function to initialize common resources used in tests
        """
        self.bowling = BowlingGame()

    def test_random_score(self):
        """
        Function to test a random score against current code with
        one strike and one spare

        Frames and scoring:
        Frame 1: 2, 2  | 4
        Frame 2: 6, 2  | 8
        Frame 3: 4, 5  | 9
        Frame 4: 10    | 10 + 1 + 0 = 11
        Frame 5: 1, 0  | 1
        Frame 6: 1, 2  | 3
        Frame 7: 6, 3  | 9
        Frame 8: 6, 4  | 10 + 3 = 13
        Frame 9: 3, 6  | 9
        Frame 10: 2, 5 | 7

        Returns:
            Passed: 74

        Raises:
            Failed: AssertionError
        """
        self.bowling.roll(2)
        self.bowling.roll(2)
        self.bowling.roll(6)
        self.bowling.roll(2)
        self.bowling.roll(4)
        self.bowling.roll(5)
        self.bowling.roll(10)
        self.bowling.roll(1)
        self.bowling.roll(0)
        self.bowling.roll(1)
        self.bowling.roll(2)
        self.bowling.roll(6)
        self.bowling.roll(3)
        self.bowling.roll(6)
        self.bowling.roll(4)
        self.bowling.roll(3)
        self.bowling.roll(6)
        self.bowling.roll(2)
        self.bowling.roll(5)
        result = self.bowling.score()
        self.assertEqual(result, 74)

    def test_rolls(self):
        """
        Function to test if all rolls are being recorded. No
        strikes or spares have been used to have a total of 20 rolls.

        Rolls:
        Rol1 1: 7
        Roll 2: 2
        Roll 3: 0
        Roll 4: 0
        Roll 5: 0
        Roll 6: 0
        Roll 7: 0
        Roll 8: 0
        Roll 9: 0
        Roll 10: 0
        Roll 11: 0
        Roll 12: 0
        Roll 13: 0
        Roll 14: 0
        Roll 15: 0
        Roll 16: 0
        Roll 17: 0
        Roll 18: 0
        Roll 19: 3
        Roll 20: 1

        Returns:
            Passed: [7, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1]

        Raises:
            Failed: AssertionError
        """
        self.bowling.roll(7)
        self.bowling.roll(2)
        for i in range(8):
            self.bowling.roll(0)
            self.bowling.roll(0)
        self.bowling.roll(3)
        self.bowling.roll(1)
        result = self.bowling.rolls
        self.assertEqual(result, [7, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1])

    def test_current_roll(self):
        """
        Function to test if the rolls are being counted and stored in
        current_roll correctly.

        Rolls:
        Rol1 1: 3
        Roll 2: 6
        Roll 3: 2

        Returns:
            Passed: 3

        Raises:
            Failed: AssertionError
        """
        self.bowling.roll(3)
        self.bowling.roll(6)
        self.bowling.roll(2)
        result = self.bowling.current_roll
        self.assertEqual(result, 3)

    def test_strike_bonus(self):
        """
        Function to test if the is_strike function initializes and then also
        the _is_strike_bonus inner function.

        Frames and scoring:
        Frame 1: 10  | 10 + 10 + 10 = 30
        Frame 2: 10  | 10 + 10 + 0 = 20
        Frame 3: 10  | 10 + 0 + 0 = 10
        Frame 4: 0   | 0
        Frame 5: 0   | 0
        Frame 6: 0   | 0
        Frame 7: 0   | 0
        Frame 8: 0   | 0
        Frame 9: 0   | 0
        Frame 10: 0  | 0

        Returns:
            Passed: 60

        Raises:
            Failed: AssertionError
        """
        self.bowling.roll(10)
        self.bowling.roll(10)
        self.bowling.roll(10)
        for i in range(7):
            self.bowling.roll(0)
            self.bowling.roll(0)
        result = self.bowling.score()
        self.assertEqual(result, 60)

    def test_spare_bonus(self):
        """
        Function to test if the is_spare function initializes and then also
        the _is_spare_bonus inner function.

        Frames and scoring:
        Frame 1: 5, 5  | 10 + 3 = 13
        Frame 2: 3, 0  | 3
        Frame 3: 0     | 0
        Frame 4: 0     | 0
        Frame 5: 0     | 0
        Frame 6: 0     | 0
        Frame 7: 0     | 0
        Frame 8: 0     | 0
        Frame 9: 0     | 0
        Frame 10: 0    | 0

        Returns:
            Passed: 16

        Raises:
            Failed: AssertionError
        """
        self.bowling.roll(5)
        self.bowling.roll(5)
        self.bowling.roll(3)
        self.bowling.roll(0)
        for i in range(8):
            self.bowling.roll(0)
            self.bowling.roll(0)
        result = self.bowling.score()
        self.assertEqual(result, 16)

    def test_frame_one(self):
        """
        Function to test if frame one will calculate an open frame correctly from the first
        two rolls.

        Frames and scoring:
        Frame 1: 8, 1  | 9
        Frame 2: 0     | 0
        Frame 3: 0     | 0
        Frame 4: 0     | 0
        Frame 5: 0     | 0
        Frame 6: 0     | 0
        Frame 7: 0     | 0
        Frame 8: 0     | 0
        Frame 9: 0     | 0
        Frame 10: 0    | 0

        Returns:
            Passed: 9

        Raises:
            Failed: AssertionError
        """
        self.bowling.roll(8)
        self.bowling.roll(1)
        for i in range(9):
            self.bowling.roll(0)
            self.bowling.roll(0)
        result = self.bowling.score()
        self.assertEqual(result, 9)

    def test_frame_ten(self):
        """
        Function to test if frame ten will calculate an open frame correctly from the last
        two rolls.

        Frames and scoring:
        Frame 1: 0     | 0
        Frame 2: 0     | 0
        Frame 3: 0     | 0
        Frame 4: 0     | 0
        Frame 5: 0     | 0
        Frame 6: 0     | 0
        Frame 7: 0     | 0
        Frame 8: 0     | 0
        Frame 9: 0     | 0
        Frame 10: 8, 1 | 9

        Returns:
            Passed: 9

        Raises:
            Failed: AssertionError
        """
        for i in range(9):
            self.bowling.roll(0)
            self.bowling.roll(0)
        self.bowling.roll(8)
        self.bowling.roll(1)
        result = self.bowling.score()
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()

