import unittest
from room_area import calculate_area


class MyTestCase(unittest.TestCase):
    def test_room_area(self):
        self.assertEqual(calculate_area(5, 4), 20)
        self.assertEqual(calculate_area(3, 7), 21)
        self.assertEqual(calculate_area(10, 10), 100)


if __name__ == "__main__":
    unittest.main()
