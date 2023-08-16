# Функции, аргументы: *args, **kwargs.
# def - definition (определение)
# DRY - don't repeat yourself


"""Создать команду вывода среднего значения оценок.
"""
data = {
    'bekzat': 3,
    'bektur': 5,
    'maxim': 5
}


def find_student(name):
    if name in data.keys():
        return True
    return False


def add(name: str, rate: int):
    if not find_student(name):
        if 5 >= rate >= 1:
            data[name] = int(rate)
        else:
            print('оценка должна быть от 1 до 5')
            return False
    else:
        print(f'имя {name} уже есть!')


def delete(name):
    if find_student(name):
        del data[name]


def edit(name, new_name):
    if find_student(name):
        data[new_name] = data.pop(name)
3

while 1:
    print(data)
    command = input(f'1) add\n'
                    f'2) delete\n'
                    f'3) edit\n')
    if command == '1':
        add(name=input(f'введите имя: '), rate=int(input('оценка: ')))
    elif command == '2':
        delete(name=input('кого удалим? '))
    elif command == '3':
        edit(name=input('кого заменить? '), new_name=input("новое имя: "))


# add('азиз', 5)

# numbers = [20, 50, 100, 200]
# names = ['т. молдо', "к. датка", "т. сатылганов", "а. осмонов"]
#
# data = dict(zip(names, numbers))
# data = {i: {b} for i, b in data.items()}
# print(data)

# def students_marks(**kwargs):
#     return kwargs
#
# print(students_marks(samat=5, adilet=4, azim=3, qwert='1, 2, 3'))


# def plus(a, *args, b=0):
#     print(a, b, args)
#     return sum(args) + a + b
#
#
# print(plus(2, 5, 3, 2,  2, 1))






# def designation(parameters):
#     expression, statement
#     return value
# designation(arguments)

# def get_square(width: int = 1, length: int = 1) -> int:
#     """Принимет 2 значения длина и ширина
#     возвращщадь прямоугольника.
#     """
#     return width * length  # возврат площади

# print(get_square.__doc__)


# square_2 = get_square()
# square_hall = get_square(length=8, width=12)
# print(square_2, square_hall, sep='\n')

# width = 6
# length = 4
# square_2 = width * length
# print(square_2)
#
# width = 12
# length = 8
# square_hall = width * length
# print(square_hall)


# word = 'python'
#
# def len1(sequence):
#     counter = 0
#     for _ in sequence:
#         counter += 1
#     return counter
#
# print(len1('geektech'))
# print(len1([2, 6, 4, 3]))


# print(5 + len('123'))


# def greet(name, surname='surname'):  # name - обязательный позиционный параметр
#     print(f'name: {name.title()}, surname: {surname.title()}')
#
#
# greet('samat', 'aliev')  # samat - обязательный позиционный аргумент
# greet(surname='bazhenova', name='alina') # именованные аргументы (keyword arguments)
