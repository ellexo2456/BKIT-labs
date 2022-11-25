import math

from lab2.lab_python_oop.color import FigureColor
from lab2.lab_python_oop.figure import Figure


class Circle(Figure):
    FIGURE_TYPE = 'Круг'

    def __init__(self, color, radios):
        if not radios > 0:
            raise ValueError
        self.radios = radios
        self.color = FigureColor(color)

    def square(self):
        return math.pi * self.radios ** 2

    def __repr__(self):
        return (
                f'{Circle.type()} '
                f'радиусом {self.radios}, площадью {self.square():.2f} '
                f'и цветом {self.color}'
            )
