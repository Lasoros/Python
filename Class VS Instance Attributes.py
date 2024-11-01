class Point:
    default_color = "red"

    def __init__(self, x, y): #__init__ is a magic method
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})") #can use self to read attributes of the current obj or call others methods said obj

Point.default_color = "yellow"

point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
#point.z = 10 can add attributes outside of contructor
point.draw()

another = Point(3, 4)
print(another.default_color)
another.draw()

#each Point has its own attributes indipendent of eachother (I.E. John and Kate both have eyes but different eye color)
#Above are called Instance Attributes
#Class level attributes are shared by all instances of that class. (I.E. All humans have 2 eyes/ears/legs/feet/etc)