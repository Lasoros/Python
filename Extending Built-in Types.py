class Text(str):
    def duplicate(self):
        return self + self

    def lower(self):
        return self + " this is lowercase now. . ."

class TrackableList(list):
    def append(self, __object):
        print("Append called")
        super().append(__object)

text = Text("Python")
print(text.lower())

print(text.duplicate())

list = TrackableList()
list.append("1")
