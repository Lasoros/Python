
# adding two __ denotes it private
# making something private is not a security measure as you are still able to access it, see below
# making something private is an alert for anyone using the class "no touch"

class TagCloud:
    def __init__(self):
        self.__tags = {}

    def __add__(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower, 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

cloud = TagCloud()

print(cloud.__dict__)

print(cloud._TagCloud__tags)

cloud.__add__('Python')

print(cloud._TagCloud__tags)