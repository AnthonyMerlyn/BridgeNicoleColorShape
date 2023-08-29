class Color:

  def apply_color(self):
    pass


class RedColor(Color):

  def apply_color(self):
    return "red"


class BlueColor(Color):

  def apply_color(self):
    return "blue"


class Shape:

  def __init__(self, color):
    self.color = color

  def apply_color(self):
    pass


class Circle(Shape):

  def apply_color(self):
    return f"This circle is {self.color.apply_color()}."


class Square(Shape):

  def apply_color(self):
    return f"This square is {self.color.apply_color()}."


# Verwendung
red_color = RedColor()
blue_color = BlueColor()

red_circle = Circle(red_color)
blue_square = Square(blue_color)

print(red_circle.apply_color())  # Ausgabe: This circle is red.
print(blue_square.apply_color())  # Ausgabe: This square is blue.