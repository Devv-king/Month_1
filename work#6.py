contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Служба спасения', 'phone': '911'},
    {'name': 'Пожарная служба', 'phone': '101'},
]


def create(name, phone):
    for contact in contacts:
        if contact.keys() == name:
            contact[phone] = phone
            print(f"Номер {name} обнавлен на {phone}.")
            return
    new_name = {"name": name, "phone": phone}
    contacts.append(new_name)
    print(f"Контакт {name} c номером {phone} добавлен.")


def edit(name):
    for contact in contacts:
        if contact["name"] == name:
            new_name = input("Введите новое имя:")
            new_phone = input("Введите новый номер:")

            for contact in contacts:
                if contact['name'] == new_name or contact['phone'] == new_phone:
                    print(f"Контакт c таким именем или номером уже есть.")
                    return

            contact['name'] = new_name
            contact['phone'] = new_phone
            print("Контакт изменен.")
            return

        print("Контакт с указанным именем не найден.")


def delete(name):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print("Контакт удален!")
            return

    print('Контакт с таким именем не найден.')


while True:
    for contact in contacts:
        print(f"Имя: {contact['name']}  |  Номер : {contact['phone']}")
    choice = input("Выберите команду: ")
    if choice == '1':
        name = input('Введите имя: ')
        phone = input('Введите номер: ')
        create(name, phone)
    elif choice == '2':
        name = input('Введите имя,которое надо изменить: ')
        edit(name)
    elif choice == '3':
        name = input('Введите имя,которое надо удалить: ')
        delete(name)
    elif choice == '4':
        print("Выход из программы.")
        break
    else:
        print("Неверная команда. Попробуйте снова!")



