# Структуры данных: словари, множества.
# {key: value}
# dict - dictionary (словарь)
# set - множество

# from random import choice
#
# students = [2, 3, 4, 6, 7, 8, 10, 11, 13, 14, 15, 16, 18, 19]
#
# students_answers = {}
#
# while len(students) != 0:
#     print(students)
#     student_id = choice(students)
#     name = input(f'имя студента под номером {student_id}: ').title()
#     rate = int(input(f'оценка для {name}: '))
#     students_answers[name] = rate
#     students.remove(student_id)
#
#
# for name, rate in students_answers.items():
#     print(f'{name}: {rate}')
#
# print(sum(students_answers.values()) / len(students_answers))




# numbers = [2, 4, 'dfg']
# numbers = set(numbers)
# print(len(numbers))

# manty = {"мясо", "тесто", "лук"}
# plov = {'рис', "морковь", "мясо"}
#
# manty.remove('тесто')
# manty.add(56)
# print(manty)

# for i in manty:
#     print(i)

# print(plov.symmetric_difference(manty))
# print(plov ^ manty)
#
# print(plov.difference(manty))
# print(plov - manty)
#
# print(plov.union(manty))
# print(plov | manty)
#
# print(plov.intersection(manty))
# print(plov & manty)

# numbers = {1, 2, 3, 4, 2, 3, 3, 1}
# numbers2 = [1, 2, 3, 4, 2, 3, 3, 1]
#
# print(type(numbers))
# print(numbers2)





# new = dict(name='Azamat', surname='Kalygulov', country='kg')
# # new = dict([[1, 2], [3, 4]])
# # print(new)
#
# student = {
#     'name': 'Jack',
#     'age': 20,
#     'hobby': ['chess', 'english', 'programming'],
#     'married': True
# }



# for i in student:
#     print(f'{i}: {student[i]}')


# print(student)


# print(student['nam'])
# print(student.get('name', 'нет такого ключа!'))

"""добавление"""
# student['weight'] = 65
# student.update(new)

"""изменение"""
# student['age'] = 21.5
# student['hobby'].append('chinese')
# student['hobby'][0] = 'boxing'
# student['hobby'].insert(1, 'football')


"""удаление"""
# del student['married']
# deleted = student.pop('hobby')
# print(deleted)
# del student['hobby'][1]

# for i, v in student.items():
#     print(f'{i} ==> {v}')

# print(student.keys())
# print(student.values())
# print(student.items())
# print(type(student))
