import sys
import math


def get_coef(index, prompt):
    """
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффициента

    Returns:
        float: Коэффициент квадратного уравнения
    """
    try:
        coef_str = sys.argv[index]
    except IndexError:
        coef_str = input(f'{prompt} ')

    while True:
        try:
            coef = float(coef_str)
            if not coef and index == 1:
                print('Коэффициент А не может принимать значение нуль!')
            else:
                break
        except ValueError:
            print('Значение должно быть действительным числом!')
        coef_str = input(f'{prompt} ')

    return coef


def get_roots(a, b, c):
    """
    Вычисление корней биквадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
    """
    result = []
    D = b * b - 4 * a * c

    if D == 0.0:
        root = -b / (2.0 * a)
        if root >= 0:
            biroot = math.sqrt(root)
            result += [
                biroot,
                -biroot
            ]

    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 >= 0:
            biroot1 = math.sqrt(root1)
            result += [
                biroot1,
                -biroot1
            ]
        if root2 >= 0:
            biroot2 = math.sqrt(root2)
            result += [
                biroot2,
                -biroot2
            ]

    result = list(set(result))
    return result


def main():
    """
    Основная функция
    """
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    roots = get_roots(a, b, c)

    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    else:
        print(
            f'Найдено {len_roots} корня:' if len_roots > 1 else 'Найден 1 корень:',
            *roots
        )


if __name__ == "__main__":
    main()
