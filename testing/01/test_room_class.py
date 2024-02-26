import unittest
from room_area_class import Room


class TestRoomArea(unittest.TestCase):
    def test_room_area(self):
        room = Room(4,3)
        self.assertEqual(room.calculate_room(), 12)


if __name__ == '__main__':
    unittest.main()
