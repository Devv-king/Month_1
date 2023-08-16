data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

del numbers[0]
letters.append(numbers.pop(0))
numbers.insert(1, 2)
numbers.reverse()
letters.reverse()
letters[1] = letters[1].upper()
letters[5] = letters[5].upper()
letters[7] = letters[7].lower()

for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2

letters = tuple(letters)
numbers = tuple(numbers)

print(letters)
print(numbers)