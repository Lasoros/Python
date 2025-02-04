from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

def draw(controls):
    for control in controls:
        control.draw()

ddl = DropDownList()
#print(isinstance(ddl, UIControl))
textbox = TextBox()
draw([ddl, textbox])

#to achieve polymorhpic behaviour you must start a base class than define the common behaviour/common method to give to its children

#create parents or base class that then has the attributes for the children defined within