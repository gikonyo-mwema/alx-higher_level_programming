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
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.

        Args:
            value (int): width of rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height of this rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height of rectangle.

        Args:
            value (int): height of rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x of this rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Property setter for x.

        Args:
            value (int): x.

        Raises:
            TypeError: if x is not an integer.
            ValueError: if x is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y of this rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Property setter for y.

        Args:
            value (int): y.

        Raises:
            TypeError: if y is not an integer.
            ValueError: if y is less than or equal to zero.
        """
        if type(value) is not int:
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
        print(
            (" " * self.__x + "#" * self.__width + "\n") *
            self.__height, end=""
        )

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return (
            f"Rectangle {self.__x}/{self.__y} - "
            f"{self.__width}/{self.height}"
        )

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
