from datetime import datetime

class Player:
    MAX_POSITION = 10
    MAX_SPEED = 3

    def __init__(self):
        self.position = 0

    def move(self, steps):
        if self.position + steps < Player.MAX_POSITION:
            self.position = self.position + steps
        else:
            self.position = 10

    def draw(self):
        drawing = "-" * self.position + "|" + "-" * (Player.MAX_POSITION - self.position)
        print(drawing)


p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()

p1, p2 = Player(), Player()
print("MAX_SPEED of p1 and p2 before assignment:")
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

p1.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
print(Player.MAX_SPEED)

# Create Players p1 and p2
p1, p2 = Player(), Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# ---MODIFY THIS LINE---
Player.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)


class BetterDate:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        # parts = datestr.split("-")
        # year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    @classmethod
    def from_datetime(cls, datetime_object):
        year, month, day = datetime_object.year, datetime_object.month, datetime_object.day
        return cls(year, month, day)


# bd = BetterDate.from_str('2020-04-30')
today = datetime.today()
bd = BetterDate.from_datetime(today)
print(bd.year)
print(bd.month)
print(bd.day)
