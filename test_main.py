"""Tests for CryptoDcaPlanner."""
import unittest
from main import calculate


class TestTool(unittest.TestCase):
    def test_main_function(self):
        self.assertAlmostEqual(calculate(50, 52), 2600, places=6)


if __name__ == "__main__":
    unittest.main()
