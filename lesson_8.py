# Работа с файлами.
# w - write запись, перезапись
# a - add дозаписи
# r - read чтение
# x - бесконфликтный режим открытия\создания файла

7, 50, 76, 73, 60, 66, 69, 68

# answers = {}
#
# with open('results.txt', 'r') as file:
#     for line in file.readlines():
#         answers[line.split()[0]] = line.split()[-1]
#         # print(line.split()[0], line.split()[-1])
#         # print(type(line))
#
# right = list(answers.values()).count("правильно")
# wrong = list(answers.values()).count("неправильно")
# print(
#     f'правильно: {right}\n'
#     f'неправильно: {wrong}\n'
#     f'правильно/неправильно {round(right * 100 / len(answers), 1)}/'
#     f'{round(wrong * 100 / len(answers), 1)}'
# )


# from random import randint, choice
# students = [1, 2, 3, 4, 7, 8, 10, 11, 13, 14, 15, 16, 18, 19]
#
# with open('results.txt', 'w') as file:
#     file.write('')
#
# while len(students) != 0:
#     print(students)
#     first = randint(1, 10)
#     second = randint(10, 101)
#     student_id = choice(students)
#     name = input(f'name {student_id}: ').title()
#     user_answer = int(input(f'сколько будет {first} * {second}'))
#     right_answer = first * second
#     if user_answer == right_answer:
#         with open('results.txt', 'a') as file:
#             file.write(
#                 f'{name}: {first} * {second} = {user_answer}'
#                 f' ({right_answer}) правильно\n'
#             )
#         print('right')
#     else:
#         with open('results.txt', 'a') as file:
#             file.write(
#                 f'{name}: {first} * {second} = {user_answer}'
#                 f' ({right_answer}) неправильно\n'
#             )
#         print(f'wrong ({right_answer})')
#     students.remove(student_id)







# with open('new.txt', 'x') as file:
#     file.write('12431242')

# file = open('file.txt', 'w', encoding='utf-8')
# file.write('Бишкек, Geektech')
# file.close()

# with open('file.txt', 'a') as file:
#     file.write('\n222222')

# from time import sleep as ukta
#
# with open('file.txt', 'r') as file:
#     for i in file.read():
#         ukta(1)
#         print(i, end='')

    # print(file.read())
    # print(file.readlines()[5])
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())


# contacts = [
#     {'name': 'aa', 'phone': '0500100200'}]
#
#
# def add(name, phone):
#     for contact in contacts:
#         if name in contact.values() and phone not in contact.values():
#             if type(contact['phone']) != list:
#                 contact['phone'] = [contact['phone']]
#                 contact['phone'].append(phone)
#             else:
#                 contact['phone'].append(phone)
#
# add('aa', '0500454554')
# add('aa', '0777112233')
# add('aa', '0555111211')
# print(contacts)