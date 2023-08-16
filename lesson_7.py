# lambda, и работа с исключениями
# lambda arguments: expression
# map, filter
# try:
#     check
# except:
#     message, define smth
# finally:
#     message, define smth

# raise, assert

# word = 'python'
#
# while True:
#     try:
#         index_user = int(input('индекс? '))
#         print(word[index_user])
#     except:
#         print(f'только цифры, от 0 до {len(word)}')
    # except IndexError:
    #     print('нет такого индекса')
    # except ValueError:
    #     print('только цифры')


# def plus(a, b):
#     return a + b
#
# assert plus(2, 3) == 6



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
#     # try:
#     if not name.isalpha():
#         raise Exception('имя должно содержать только буквы!')
#     rate = int(input(f'оценка для {name}: '))
#     # except:
#     print('только цифры!')
#         # continue
#     students_answers[name] = rate
#     students.remove(student_id)
#
#
# for name, rate in students_answers.items():
#     print(f'{name}: {rate}')
#
# print(sum(students_answers.values()) / len(students_answers))





# try:
#     print(name)
# except:
#     print('нет такой переменной')
#     тфьу = "эфяфьфе"
# finally:
#     print('проверка завершена')

# print(10/0)
# print('123'[5])
# print(2 + 'a')
# print(int('sdf'))


# numbers = list(range(1, 11))
# new = sorted(numbers, key=lambda x: x % 2 == 0)
# print(new)

# new = tuple(filter(lambda x: x > 4, numbers))
# new = [i for i in numbers if i > 6]
# print(new)

# print(numbers)
# new = list(map(lambda x: x * 2, numbers))
# print(new)

plus_lambda = lambda c, b: c + b
#
#
# def plus(a, b):
#
#     return a + b
#
# print(type(plus_lambda))
# print(type(plus))

# print(a(2, 3))
print(plus_lambda(2, 3))


# def up_letter(word):
#     return word.title()
#
#
# def last_up(word):
#     return word[:-1] + word[-1].title()
#
#
# def show_words(func, word):
#     for i in word:
#         print(func(i))
#
#
# show_words(lambda word: word[:-1] + word[-1].title(), ('isabek', 'azim', 'tima'))

# show_words(lambda word: word.title(), ('islam', 'azat', 'timur'))


# show_words(up_letter, 'python')
# show_words(up_letter, ['bishkek', 'kgz', 'geektech'])
# show_words(len, ['bishkek', 'kgz', 'geektech'])
