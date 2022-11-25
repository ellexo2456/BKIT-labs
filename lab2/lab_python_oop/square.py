from lab2.lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    FIGURE_TYPE = 'Квадрат'

    def __init__(self, color, side):
        self._side = side
        super().__init__(color, side, side)

    def __repr__(self):
        return (
                f'{Square.type()} '
                f'со стороной {self._side}, площадью {self.square()} '
                f'и цветом {self.color}'
            )
