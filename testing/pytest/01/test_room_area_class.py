from room_area_class import Room
import pytest

def test_room_area_valid():
    room = Room(4,3)
    area = room.calculate_room()
    assert area == 12

def test_room_area_invalid():
    with pytest.raises(ValueError) as e:
        room = Room(-4,3)
    assert str(e.value) == "Width and Length must be positive values"