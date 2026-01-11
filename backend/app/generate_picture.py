import random
from PIL import Image, ImageDraw

class GeneratePicture:
    def __init__(self, WIDTH=800, HEIGHT=600):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        factor = (self.WIDTH * self.HEIGHT) // 5000
        self.SHAPES = random.randint(250 * factor, 500 * factor)
        self.img = Image.new("RGB", (self.WIDTH, self.HEIGHT), self._random_color())
        self.draw = ImageDraw.Draw(self.img)
    
    def _random_color(self):
        return tuple(random.randint(0, 255) for _ in range(3))
    
    def _draw_rectangle(self):
        x1, y1 = random.randint(0, self.WIDTH), random.randint(0, self.HEIGHT)
        x2, y2 = random.randint(x1, self.WIDTH), random.randint(y1, self.HEIGHT)
        self.draw.rectangle([x1, y1, x2, y2], fill=self._random_color(), outline=None)
    def _draw_circle(self):
        x, y = random.randint(0, self.WIDTH), random.randint(0, self.HEIGHT)
        r = random.randint(10, 100)
        self.draw.ellipse([x-r, y-r, x+r, y+r], fill=self._random_color())
    def _draw_line(self):
        x1, y1 = random.randint(0, self.WIDTH), random.randint(0, self.HEIGHT)
        x2, y2 = random.randint(0, self.WIDTH), random.randint(0, self.HEIGHT)
        self.draw.line([x1, y1, x2, y2], fill=self._random_color(), width=random.randint(1, 6))
    def _draw_polygon(self):
        points = [
            (random.randint(0, self.WIDTH), random.randint(0, self.HEIGHT))
            for _ in range(random.randint(3, 8))
        ]
        self.draw.polygon(points, fill=self._random_color())
    
    def _generate_shape(self, type):
        strategy = {
            "rect": self._draw_rectangle,
            "circle": self._draw_circle,
            "line": self._draw_line,
            "polygon": self._draw_polygon
        }
        draw_method = strategy.get(type)
        if draw_method:
            draw_method()
     
    def generate_picture(self):
        shape_types = ["rect", "circle", "line", "polygon"]
        for _ in range(self.SHAPES):
            shape_type = random.choice(shape_types)
            self._generate_shape(shape_type)
        return self.img
