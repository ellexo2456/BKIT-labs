import json
from random import randint
from print_result import print_result
from cm_timer import cm_timer


@print_result
def f1(arg):
    return sorted([row['job-name'].lower() for row in arg])


@print_result
def f2(arg):
    return list(filter(lambda s: 'программист' in s, arg))


@print_result
def f3(arg):
    return (lambda job: list(map(lambda s: s + ' с опытом Python', job)))(arg)


@print_result
def f4(arg):
    job_with_sal = zip(arg, [f'зарплата {randint(100000, 200000)} руб.' for _ in range(len(arg))])
    return list(map(lambda s: ', '.join(s), job_with_sal))


if __name__ == '__main__':
    with open('data_light.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    with cm_timer():
        f4(f3(f2(f1(data))))
