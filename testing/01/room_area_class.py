class Room():
  def __init__(self, width, length):
    self.width = width
    self.length = length

  def calculate_room(self):
    return self.width * self.length
if __name__ == '__main__':
    room = Room(2,7)
    print(room.calculate_room())
