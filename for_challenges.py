# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки
# from unicodedata import name


def get_text_names(names, count_bool=False):
    text_names = ""
    for name in names:
        if count_bool:
            text_names += name + ": " + str(len(name)) + "\n"
        else:
            text_names += name + "\n"
    return text_names


def get_names_male(names, is_male):
    text_conclusion = ""
    for name in names:
        if is_male[name]:
            text_conclusion += name + ": пол мужской\n"
        else:
            text_conclusion += name + ": пол женский\n"
    return text_conclusion


def get_count_group(groups):
    text_conclusion = ""
    for group in groups:
        text_conclusion += (
            "Группа " + str(groups.index(group) + 1) + ": " + str(len(group)) + "\n"
        )
    return text_conclusion


def get_element_group(groups):
    text_conclusion = ""
    for group in groups:
        text_conclusion += "Группа " + str(groups.index(group) + 1) + ": "
        for element in group:
            if element == group[-1]:
                text_conclusion += element
            else:
                text_conclusion += element + ", "
        text_conclusion += "\n"

    return text_conclusion


if __name__ == "__main__":
    # Задание 1
    # Необходимо вывести имена всех учеников из списка с новой строки

    names = ["Оля", "Петя", "Вася", "Маша"]
    print(get_text_names(names))

    # Задание 2
    # Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
    # Пример вывода:
    # Оля: 3
    # Петя: 4
    names = ["Оля", "Петя", "Вася", "Маша"]
    print(get_text_names(names, True))

    # Задание 3
    # Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

    is_male = {
        "Оля": False,  # если False, то пол женский
        "Петя": True,  # если True, то пол мужской
        "Вася": True,
        "Маша": False,
    }
    names = ["Оля", "Петя", "Вася", "Маша"]
    print(get_names_male(names, is_male))

    # Задание 4
    # Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
    # Пример вывода:
    # Всего 2 группы.
    # Группа 1: 2 ученика.
    # Группа 2: 4 ученика.

    groups = [
        ["Вася", "Маша"],
        ["Вася", "Маша", "Саша", "Женя"],
        ["Оля", "Петя", "Гриша"],
    ]
    print(get_count_group(groups))
    # Задание 5
    # Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
    # Пример вывода:
    # Группа 1: Вася, Маша
    # Группа 2: Оля, Петя, Гриша

    groups = [
        ["Вася", "Маша"],
        ["Оля", "Петя", "Гриша"],
        ["Вася", "Маша", "Саша", "Женя"],
    ]
    print(get_element_group(groups))
