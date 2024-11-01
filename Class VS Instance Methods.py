class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod #<----- called a decorator
    def zero(cls): #when defining a class method call its first parameter 'cls' (class)
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero() #for thie example, point = Point.zero() is a factory method as it creates a new obh
point.draw()