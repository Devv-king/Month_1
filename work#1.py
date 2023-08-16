o1 = float(input("Чуй: "))
o2 = float(input("Ош: "))
o3 = float(input("Нарын: "))
o4 = float(input("Талас: "))
o5 = float(input("Баткен: "))
o6 = float(input("Ыссык-Кол: "))
o7 = float(input("Джалал-Абад: "))
sum_wat = o1 + o2 + o3 + o4 + o5 + o6 + o7
aver_wat = sum_wat / 7
print(f'Средний показатель температуры воздуха по КР на сегрдня {round(aver_wat, 2)}')