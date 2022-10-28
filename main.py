from operator import itemgetter


class Faculty:
    def __init__(self, name, id, university_id, students_count):  # Constructor
        self.name = name
        self.id = id
        self.university_id = university_id
        self.students_count = students_count


class University:
    def __init__(self, id, name):  # Constructor
        self.id = id
        self.name = name


# Многие-ко-многим
class FacultyUniversity:
    def __init__(self, faculty_id, university_id):  # Constructor
        self.faculty_id = faculty_id
        self.university_id = university_id


# Students
university = [
    University(1, "BMSTU"),
    University(2, "SPSU"),
    University(3, "Moscow State University"),
    University(4, "Novosibirsk State University"),
    University(5, "TSU"),
]

# Groups
faculty = [
    Faculty("FN4", 1, 1, 1000),
    Faculty("Georgafical", 2, 2, 2343),
    Faculty("mathematical", 3, 4, 3524),
]

# Students and Groups
faculty_university = [
    FacultyUniversity(1, 1),
    FacultyUniversity(1, 2),
    FacultyUniversity(2, 3),
    FacultyUniversity(3, 4),
    FacultyUniversity(3, 5),
]


# University и Faculty связаны отношением один-ко-многим.
# Выведите список всех университетов, у которых в названии присутствует
# слово "University", и факультетов в них.

def task1():
    result = []
    for i in university:
        middle_result = []
        if "University" in i.name:
            middle_result.append(i.name)
            for j in faculty:
                if j.university_id == i.id:
                    middle_result.append(j.name)
            result.append(middle_result)
    return result


# University и Faculty связаны отношением один-ко-многим.
# Выведите список всех университетов со средним количеством студентов в каждом факультете,
# отстортированный по среднему количеству. Среднее количество должно быть округлено до 2 знаков после запятой

def task2():
    result = []
    for i in university:
        sum = 0
        count = 0
        for j in faculty:
            if j.university_id == i.id:
                sum += j.students_count
                count += 1
        if (count == 0):
            result.append((i.name, 0))
        else:
            result.append((i.name, round(sum / count, 2)))
    return sorted(result, key=itemgetter(1), reverse=True)


# University и Faculty связаны отношением многие-ко-многим.
# Выведите список всех факультетов, у которых название начинается с буквы "G",
# и список вузов, в которых имеется такой факультет.

def task3():
    result = []
    for i in faculty:
        if i.name[0] == "G":
            result.append(i.name)
            for j in faculty_university:
                if i.id == j.university_id:
                    for k in university:
                        if j.university_id == k.id:
                            result.append(k.name)
    return result


def main():
    print("\nTask 1:")
    print(task1())

    print("\nTask 2:")
    print(task2())

    print("\nTask 3:")
    print(task3())


if __name__ == '__main__':
    main()
