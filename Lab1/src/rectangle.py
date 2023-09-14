"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def set_values(self, x, y):
        pass

    @abstractmethod
    def area(self):
        pass



class Rectangle(Shape):
    def __init__(self, width, height):
    # To create a private variable, you prefix the variable name with two underscores.
    # The comment above cited from https://blog.gitnux.com/code/python-private-variables/
        self.__width = width
        self.__height = height

    def set_values(self, x, y):
        self.__width = x
        self.__height = y

    def area(self):
        return self.__width * self.__height

    # Getter and setter for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle(3, 4)

    # Print out the area function
    print("area:", rect.area())
