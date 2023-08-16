ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, ten))
square = list(map(lambda x: x ** 2, evens))
print(ten)
print(evens)


def get_index(obj):
    while True:
        try:
            number_index = input("Input index: ")
            if number_index != 'exit':
                print(obj[int(number_index) - 1])
            else:
                break
        except IndexError:
            print(f"Indexes are only numbers. Size from 1 to {len(evens)}")
        except ValueError:
            print("Indexes are only numbers.")


get_index(evens)
