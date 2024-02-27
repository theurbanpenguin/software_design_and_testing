import unittest
from room_area_class import Room


class TestRoomArea(unittest.TestCase):
    def test_room_area_postive_values(self):
        room = Room(4, 3)
        self.assertEqual(room.calculate_room(), 12)

    def test_negative_dimensions(self):
        # Test for negative width
        with self.assertRaises(ValueError):
            Room(-4, 3)

        # Test for negative length
        with self.assertRaises(ValueError):
            Room(4, -3)

        # Test for negative width and length
        with self.assertRaises(ValueError):
            Room(-4, -3)


if __name__ == "__main__":
    unittest.main()
