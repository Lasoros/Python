class TagCloud:
    def __init__(self):
        self.tags = {}

    def __add__(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower, 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)

cloud = TagCloud()

cloud.__add__("Python")
cloud["python"] = 10
cloud.__add__("python")
cloud.__add__("python")

print(cloud.tags)

