from lab2.lab_python_oop.color import FigureColor
from lab2.lab_python_oop.figure import Figure


class Rectangle(Figure):
    FIGURE_TYPE = 'Прямоугольник'

    def __init__(self, color, a, b):
        if a <= 0 or b <= 0:
            raise ValueError
        self._a, self._b = a, b
        self.color = FigureColor(color)

    def square(self):
        return self._a * self._b

    def __repr__(self):
        return (
                f'{Rectangle.type()} '
                f'длиной {self._a}, шириной {self._b}, '
                f'площадью {self.square()} и цветом {self.color}'
            )
