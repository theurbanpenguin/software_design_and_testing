import unittest
from employees import Manager


class TestFullName(unittest.TestCase):
    def test_full_name(self):
        e = Manager("Vera", "Wang", 0, None)
        self.assertEqual(e.get_full_name(), "Vera Wang")  # add assertion here


if __name__ == "__main__":
    unittest.main()
