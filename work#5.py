operators = {}
data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []

for i in data:
    if i.isnumeric():
        codes.append(i)
    else:
        designations.append(i)

i = 0
while i < len(codes):
    operators[designations[i]] = {codes[i]}
    i += 1

del operators['Katel']
del operators['Fonex']
operators['O!'].update({'0700', '0500'})
operators['Megacom'].update({'0999', '0555'})
operators['Beeline'].update({'0222', '0777'})

for i, v in operators.items():
    print(f'{i} - {v}')

# Домашнее задание № 5
"""
Дан кортеж состоящий из номеров и кодов:

data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

Создать два пустых списка designations и codes

Пройтись циклом for по кортежу data, добавить наименования компаний в designations и коды в codes

Создать словарь operators на основе списков designations и codes c помощью цикла while, где ключами будут названия 

    компаний а значениями коды содержащиеся в множестве (set)!

Удалить нефункционирующие операторы из словаря operators. (Katel, Fonex)

Добавить/Обновить к уже существующим номерам (Ошке, Меге и Билайну) пару кодов содержащихся в множестве. Добавить,
    а не просто переписать вручную в сэт.

В итоге вывести на экран наименования операторов и соответствующие номера в таком виде (в паре ключ-значение):
"""
