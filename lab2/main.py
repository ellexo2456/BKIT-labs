from lab2.lab_python_oop.circle import Circle
from lab2.lab_python_oop.rectangle import Rectangle
from lab2.lab_python_oop.square import Square

if __name__ == '__main__':
    variant = int(input('Введите номер своего варианта (int): '))

    rect = Rectangle('blue', variant, variant)
    cir = Circle('green', variant)
    sqr = Square('red', variant)

    print(rect)
    print(cir)
    print(sqr)
