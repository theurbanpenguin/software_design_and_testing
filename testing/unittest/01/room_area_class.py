class Room:
    def __init__(self, width, length):
        if width < 0 or length < 0:
            raise ValueError("Width and Length must be positive values")
        self.width = width
        self.length = length

    def calculate_room(self):
        return self.width * self.length


if __name__ == "__main__":
    room = Room(3, 7)
    print(room.calculate_room())
