#!/usr/bin/python3
"""
This is the 'rectangle' module.

The rectangle module supplies one class, Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int, optional): the x cordinate
            y (int, optional): the y cordinate
            id (int, optional): the identity
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = height
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be >= 0")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not  isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and output the area of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle instance with #"""
        print("\n" * self.__y, end="")
        print((" " * self.__x + "#" * self.__width + "\n") * self.__height, end="")

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.height}"

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute."""
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)

        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
    def to_dictionary(self):
        """
        Return the dictionary representation of a Rectangle instance.
        Returns
        dict
            Dictionary representation of a Rectangle instance.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
