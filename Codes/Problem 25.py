class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth


length = int(input("Please enter the length - \n"))
breadth = int(input("Please enter the Breadth - \n"))
rect = Rectangle(length, breadth)

print("Area is - ", rect.area())