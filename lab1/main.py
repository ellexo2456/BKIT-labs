import sys
import cmath


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

    try:
        coef = float(coef_str)
    except ValueError:
        print('Значение должно быть действительным числом!')

    return coef


def get_roots(a, b, c):
    """
    Вычисление корней биквадратного уравнения
    с учётом комплексных вариантов

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
        biroot = cmath.sqrt(root)
        result += [
            biroot,
            -biroot
        ]

    elif D > 0.0:
        sqD = cmath.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        biroot1 = cmath.sqrt(root1)
        biroot2 = cmath.sqrt(root2)
        result += [
            biroot1,
            -biroot1,
            biroot2,
            -biroot2
        ]

    result = set(result)
    result = [_.real if not _.imag else _ for _ in result]
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
