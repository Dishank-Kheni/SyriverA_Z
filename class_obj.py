class Point:
    default_color = "Red"  # class level attribute

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def draw(self):
        print(f'point {self.x,self.y}')

    @classmethod
    def zero(cls):
        return cls(0, 0)

    # Magic methods
    def __str__(self) -> str:  # return an object
        return f"x = {self.x}, y = {self.y}"

    # comparing two objects
    def __eq__(self, obj) -> bool:
        return self.x == obj.x and self.y == obj.y

    # greater than cmp
    def __gt__(self, obj):
        return self.x > obj.x and self.y > obj.y

    # add two objects
    def __add__(self, obj):
        return Point(self.x+obj.x, self.y+obj.y)


point = Point(2, 3)  # calss, obj and constructor

# class vs Instance attribute
print(Point.default_color)
print(point.default_color)
Point.default_color = "Yellow"
print(point.default_color)
point.draw()

# class vs Instance methods
point1 = Point.zero()
point1.draw()

# magic methods
# google : python 3 magic methods
print(point)

# comparing object, bydefault python compares addresses of the object
print(point == point1)  # cmp objects
print(point > point1)  # cmp objects
print(point < point1)  # cmp objects
print(point + point1)  # arithmatuc operations


# container class
class TagCloud:
    def __init__(self) -> None:
        self.tags = {}

    def __add__(self, tag):
        self.tags[tag.lower()] = self.tags[tag.lower()] + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag] = count

    def __str__(self) -> str:
        return self.tags


cloud = TagCloud()
cloud["Python"] = 10
# cloud["Python"]
# cloud["Python"]

print(cloud["Python"])
