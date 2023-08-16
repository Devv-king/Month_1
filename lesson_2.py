# Логический тип данных, условные конструкции и операторы.
# bool - boolean (логический тип данных)
# or, and, not - логические операторы
# ==, !=, >=, <=, >, < - операторы сравнения
# +=, -=, *= - операторы назначения
# if, elif, else
# is, in
# [start:stop:step]

signal = input('введите сигнал светофора!')

if signal == 'green':
    print('go')
elif signal == 'yellow' or signal == 'red':
    print('stop')
else:
    print('look at situation!')
    situation = input('опишите ситуацию на перекрестке: \n'
                      '1) off 2) traffic_police')
    if situation == '1':
        print('смотрите на право')
    elif situation == '2':
        print('слушать гаишника!')


# word = '123456789'
# print('4' in word, '8' in word)

# print('8' in word)

# new_w = word[::1]
# print(id(word))
# print(id(new_w))

# new_w = word[::-1]
#
#
# print(24 is 20+4)
# print(24 == 20+4)





# word = 'python'
# first = word[:3]
# second = word[2:]
#
# print(word)
# print(first + 'oop')
# print(second + 'qwe')

# a = int(input('number '))
# b = int(23.7) #int(input(23.7))
# print(a + b)
# word = input('введите время: ')

# print('word'.startswith('W'))
# print('word'.endswith('d'))

# print('123'.isnumeric())
# print('123'.isdigit())
# print('123'.isdecimal())


# """ДОП ЗАДАНИЕ
# создать возможность высчитывания часа
# """
#
# time = input('введите время: ').lower()
# hour = int(time[:2])
# minute = int(time[3:])
#
# if time == 'morning' or time == 'утро':
#     print('good morning')
# elif time == 'day' or time == 'день':
#     print('good afternoon')
# elif time == 'evening' or time == 'вечер':
#     print('good evening')
# else:
#     print('hello')




# print(word)
# print(hour, minute, sep='\n')


# number = ''
# print(bool(number))
# print(bool(0))
# print(bool(4))
# print(bool(0.0))
# print(bool(-0.1))

# print(number.isalpha())
# print(number.isnumeric())
# print(number.isnumeric())

# print(not True)
# print(not False)

# password = input('введите пароль! ')
#
# if len(password) >= 7 and not password.isnumeric() and not password.isalpha():
#     print('ok')
#     # print('длина пароля не подходит!')
# else:
#     print('no')


# a = 10
# # a = a + 5
# a *= 6
# print(a)

# print(2 > 7)
# print(2 != 3 and 2 > 1)
# print(3 != 2 > 1)
# print(2 != 3)
# print(2 <= 5)
# print(2 < 5 or 2 == 5)
# print(type(2 < 6))
