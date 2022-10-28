from termcolor import colored


class FigureColor:
    def __init__(self, color='red'):
        self._color = color
        try:
            self._str_color = colored(color, color=color)
        except KeyError:
            raise KeyError(f'Неверно указан цвет {color}')

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        try:
            self._str_color = colored('Color', color=value)
        except KeyError:
            raise KeyError(f'Неверно указан цвет {value}')

    def __repr__(self):
        return self._str_color
