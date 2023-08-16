# rus_alph = "йцукенгшщзхъфывапролджэячсмитьбю"
# eng_alph = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
#
# letter = 'w'
# ind = eng_alph.index(letter)
# print(rus_alph[ind])

# while True:
#     word = input('\nвведите слово: ').lower()
#     if word == 'exit' or word == 'выход':
#         print('\nзавершение...')
#         break
#     for letter in word:
#         if letter in rus_alph:
#             print(eng_alph[rus_alph.index(letter)], end='')
#         else:
#             print(rus_alph[eng_alph.index(letter)], end='')



# cash = 100
# percents = 0.05
# years = 5
#
# print(cash)
#
# for i in range(1, years+1):
#     cash += cash * percents
#     print(f'годы: {i} >> {round(cash, 2)}')

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)


# b = 20
# for i in range(11):
#     if i % 2 == 0:
#         print(i)
# print(b)

# word = 'python'
# for letter in word:
#     # if letter == 'h':
#         # break
#         # continue
#     print(letter)


#
# c = 0
# r = 1
# while c != len(word):
#     print(f"круг {r}: {word[c]}")
#     c += 1
#     r += 1

# rounds = 5
# while rounds != 0:
#     print(rounds)
#     rounds -= 1
#
# while True:
#     print('hello')
#     break


# c = 0
# k = 0
# while c != 3:
#     c += 1
#     while k != 3:
#         k += 1
#         print(c, k)


# while c < 100:
#     c += 1
#     # if c == 20 or c == 30:
#     if c in [20, 30]:
#         # break
#         continue
#     print('hello', c)


print(4 * 100 / 6)


# while True:
#     signal = input('введите сигнал светофора!')
#
#     if signal == 'green':
#         print('go')
#     elif signal == 'yellow' or signal == 'red':
#         print('stop')
#     else:
#         print('look at situation!')
#         situation = input('опишите ситуацию на перекрестке: \n'
#                           '1) off 2) traffic_police')
#         if situation == '1':
#             print('смотрите на право')
#         elif situation == '2':
#             print('слушать гаишника!')