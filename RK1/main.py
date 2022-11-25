from random import choice


def get_rand_address():
    streets = [
        'Берёзовая', 'Барвинка', 'Баррикадная', 'Бархотская', 'Барьерная', 'Баумана', 'Бахчиванджи', 'Бахчиванджи',
        'Октябрьская', 'Лобачевского', 'Лобкова', 'Лодыгина', 'Ломоносова', 'Лоцмановых', 'Лощинка', 'Луганская',
        'Союзная', 'Специалистов', 'Спутников', 'Спутников', 'Среднеуральская', 'Станционная', 'Стартовая'
    ]
    return f'ул. {choice(streets)}, стр. {choice(range(1, 100))}'


class Driver:
    """Водитель"""

    def __init__(self, id, fio, price_auto, fleet_id):
        self.id = id
        self.fio = fio
        self.price_auto = price_auto
        self.fleet_id = fleet_id


class Fleet:
    """Автопарк"""

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address


class FleetsDrivers:
    """
    'Водители автопарка' для реализации
    связи многие-ко-многим
    """

    def __init__(self, fleet_id, driver_id):
        self.driver_id = driver_id
        self.fleet_id = fleet_id


# Автопарки
fleets = [
    Fleet(1, 'автобусный автопарк', get_rand_address()),
    Fleet(2, 'автопарк "У дома"', get_rand_address()),
    Fleet(3, 'легковой автопарк', get_rand_address()),

    Fleet(11, 'стояночный автопарк', get_rand_address()),
    Fleet(22, 'грузовой автопарк', get_rand_address()),
    Fleet(33, '"Территория авто"', get_rand_address()),

]

# Водители
drivers = [
    Driver(1, 'Артамонов К. Б.', 250000, 1),
    Driver(2, 'Петров Л. А.', 350000, 2),
    Driver(3, 'Авашев И. И.', 450000, 3),
    Driver(4, 'Иваненко Ю. Г.', 350000, 3),
    Driver(5, 'Артемьев И. Р.', 250000, 3),
]

fleets_drivers = [
    FleetsDrivers(1, 1),
    FleetsDrivers(2, 2),
    FleetsDrivers(3, 3),
    FleetsDrivers(3, 4),
    FleetsDrivers(3, 5),

    FleetsDrivers(11, 1),
    FleetsDrivers(22, 2),
    FleetsDrivers(33, 3),
    FleetsDrivers(33, 4),
    FleetsDrivers(33, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [
        (f.name, f.address, d.fio, d.price_auto)
        for d in drivers
        for f in fleets
        if d.fleet_id == f.id
    ]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [
        (d.fio, d.price_auto, fd.driver_id, fd.fleet_id)
        for d in drivers
        for fd in fleets_drivers
        if d.id == fd.driver_id
    ]

    many_to_many = [
        (f.name, f.address, d_fio, d_price)
        for d_fio, d_price, d_id, f_id in many_to_many_temp
        for f in fleets
        if f.id == f_id
    ]

    print('Задание E1')
    data = list(filter(lambda f: 'автопарк' in f[0].lower(), one_to_many))
    f_names = {f_name: [] for f_name, *_ in data}
    [f_names[f_name].append(others[1:]) for f_name, *others in data]
    for k, v in f_names.items():
        print(f'{k}')
        [print(f' ⊢ Фамилия: {el[0]}, стоимость авто: {el[1]} руб.') for el in v]

    print('\nЗадание E2')
    f_names = {f_name: [] for f_name, *_ in data}
    [f_names[f_name].append(others[1:]) for f_name, *others in data]
    for k, v in f_names.items():
        mean = sum(price for _, price in v) / len(v)
        print(f'{k} — средняя стоимость авто: {mean:.2f} руб.')
        [
            print(f' ⊢ Фамилия: {el[0]}, стоимость авто: {el[1]} руб.')
            for el in sorted(v, key=lambda x: abs(mean - x[1]))
        ]

    print('\nЗадание E3')
    drivers_fleets = {d.fio: [] for d in filter(lambda d: d.fio[0] == 'А', drivers)}
    for d in drivers_fleets:
        for f_name, f_address, d_fio, d_price in many_to_many:
            if d == d_fio:
                drivers_fleets[d].append((f_name, f_address))
        print(f'{d}')
        [print(f' ⊢ {f_name} ({f_address})') for f_name, f_address in drivers_fleets[d]]


if __name__ == '__main__':
    main()
