from room_area import calculate_area


def test_room_area():
    area = calculate_area(4, 3)
    assert area == 12
