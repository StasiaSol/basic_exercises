def get_count_text(students):
    new_list = []
    text_count = ""
    for student in students:
        if student in new_list:
            continue
        else:
            text_count += (
                student["first_name"] + ": " + str(students.count(student)) + "\n"
            )
            new_list.append(student)
    return text_count


def get_max_count(students):
    max_count = 0
    for student in students:
        count_student = students.count(student)
        if count_student > max_count:
            element_list = student
            max_count = count_student
    return element_list["first_name"]


def count_girl_boy(school, is_male):
    text_result = ""
    for classes in school:
        text_result += "Класс " + classes["class"] + ":"
        count_girls = 0
        count_boys = 0
        for student in classes["students"]:
            if is_male[student["first_name"]]:
                count_boys += 1
            else:
                count_girls += 1
        text_result += (
            " девочки " + str(count_girls) + ", мальчики " + str(count_boys) + "\n"
        )
    return text_result


def max_count_students(school, is_male):
    list_result = ["Больше всего мальчиков в классе", "Больше всего девочек в классе"]
    for classes in school:
        count_girls = 0
        count_boys = 0
        for student in classes["students"]:
            if is_male[student["first_name"]]:
                count_boys += 1
            else:
                count_girls += 1
        if count_boys > count_girls:
            list_result[0] += classes["class"] + " "
        else:
            list_result[1] += classes["class"] + " "
    return list_result[0] + "\n" + list_result[1]


if __name__ == "__main__":

    # Задание 1
    # Дан список учеников, нужно посчитать количество повторений каждого имени ученика
    # Пример вывода:
    # Вася: 1
    # Маша: 2
    # Петя: 2

    students = [
        {"first_name": "Вася"},
        {"first_name": "Петя"},
        {"first_name": "Маша"},
        {"first_name": "Маша"},
        {"first_name": "Петя"},
    ]
    print(get_count_text(students))
    # ???

    # Задание 2
    # Дан список учеников, нужно вывести самое часто повторящееся имя
    # Пример вывода:
    # Самое частое имя среди учеников: Маша
    students = [
        {"first_name": "Вася"},
        {"first_name": "Петя"},
        {"first_name": "Маша"},
        {"first_name": "Маша"},
        {"first_name": "Оля"},
    ]
    # ???
    print("Самое частое имя среди учеников: " + get_max_count(students))

    # Задание 3
    # Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
    # Пример вывода:
    # Самое частое имя в классе 1: Вася
    # Самое частое имя в классе 2: Маша

    school_students = [
        [  # это – первый класс
            {"first_name": "Вася"},
            {"first_name": "Вася"},
        ],
        [  # это – второй класс
            {"first_name": "Маша"},
            {"first_name": "Маша"},
            {"first_name": "Оля"},
        ],
        [  # это – третий класс
            {"first_name": "Женя"},
            {"first_name": "Петя"},
            {"first_name": "Женя"},
            {"first_name": "Саша"},
        ],
    ]
    for class_students in school_students:
        print(
            "Самое частое имя в классе "
            + str(school_students.index(class_students) + 1)
            + ": "
            + get_max_count(students)
        )


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {"class": "2a", "students": [{"first_name": "Маша"}, {"first_name": "Оля"}]},
    {"class": "2б", "students": [{"first_name": "Олег"}, {"first_name": "Миша"}]},
    {
        "class": "2б",
        "students": [
            {"first_name": "Даша"},
            {"first_name": "Олег"},
            {"first_name": "Маша"},
        ],
    },
]
is_male = {
    "Олег": True,
    "Маша": False,
    "Оля": False,
    "Миша": True,
    "Даша": False,
}
print(count_girl_boy(school, is_male))


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {"class": "2a", "students": [{"first_name": "Маша"}, {"first_name": "Оля"}]},
    {"class": "3c", "students": [{"first_name": "Олег"}, {"first_name": "Миша"}]},
]
is_male = {
    "Маша": False,
    "Оля": False,
    "Олег": True,
    "Миша": True,
}
print(max_count_students(school, is_male))
