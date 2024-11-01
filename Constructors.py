class Point:
    def __init__(self, x, y): #__init__ is a magic method
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})") #can use self to read attributes of the current obj or call others methods said obj

point = Point(1, 2)
point.draw()

#methods defined in a class should have at least one parameter, conventionally called "self", which references the current point obj working with