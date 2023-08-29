class DrawingAPI:

  def draw_circle(self, x, y, radius):
    pass


class SVGAPI(DrawingAPI):

  def draw_circle(self, x, y, radius):
    print(f"Drawing SVG circle at ({x}, {y}) with radius {radius}")


class CanvasAPI(DrawingAPI):

  def draw_circle(self, x, y, radius):
    print(f"Drawing canvas circle at ({x}, {y}) with radius {radius}")


class Shape:

  def __init__(self, drawing_api):
    self.drawing_api = drawing_api

  def draw(self, x, y, radius):
    self.drawing_api.draw_circle(x, y, radius)


circle = Shape(SVGAPI())
circle.draw(10, 20, 5)  # Output: Drawing SVG circle at (10, 20) with radius 5

another_circle = Shape(CanvasAPI())
another_circle.draw(
    30, 40, 7)  # Output: Drawing canvas circle at (30, 40) with radius 7
