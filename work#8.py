lower_index = 0
upper_index = 100
count = 0

value = int(input("Input number: "))

with open('file.txt', 'w') as file:
    file.write(f'Отгадай число!')

while True:
    mid = (lower_index + upper_index) // 2
    print(mid)
    answer = str(input("ANSWER: "))
    count += 1

    if answer == 'yes':
        print(f"Right Number! {value} == {mid}")
        with open('file.txt', 'a') as file:
            file.write(f'Кол-во попыток: {count}\n'
                       f'Загаданное число: {value} == {mid}')
        break

    elif answer == 'up':
        lower_index = mid + 1
        with open('file.txt', 'a') as file:
            file.write(f"Предположение программы: '{mid}'\n")

    elif answer == 'low':
        upper_index = mid - 1
        with open('file.txt', 'a') as file:
            file.write(f"Предположение программы: '{mid}'\n")

    else:
        print('Попробуйте еще раз!')
