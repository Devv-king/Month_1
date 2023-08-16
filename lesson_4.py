# Структуры данных: списки, срезы, кортежи.
# list - список
# tuple - кортеж
# [start:stop:step]

# objects = (23, 45, 67.2, 56, 12)
# print(min(objects))
# print(max(objects))
# print(sum(objects))


# new = objects[:3]
#
# print(new)
# print(objects)

# objects += (5, 6, 3)

# objects = list(objects)
# objects.append(234)
# objects = tuple(objects)

# print(type(objects))


# numbers = list(range(1, 11))
# print(numbers)

# print(words[3])
# new = words[1:-1]
# print(new)

# new_numbers = [i for i in range(1, 6) if i > 3]
# print(new_numbers)
# # words = [2, 3.8, 44.9, 2.3, 1, 34]
# words = ["python", 'geektech', 'apple', 'oop']
#
# new_copy = words.copy()
#
# new_copy[0] = 566
#
# print(new_copy is words)
# print(new_copy == words)
# print(id(new_copy), id(words))
#
# print(words)
# print(new_copy)

# words.sort(key=len, reverse=True)
# words.reverse()


"""удаление"""
# del words[:2]
# words.remove('python')
# deleted = words.pop(-1)
# print(deleted)

"""добавление"""
# words.append('last')
# words.insert(4, 'for')
# words.extend(new_numbers)
# words += new_numbers

"""изменение"""
# words[1] = 200
# words[0], words[6] = words[6], words[0]
# words[4:6] = [10, 15]


# print(type(words))
# print(type(numbers))
