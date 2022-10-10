# Второй способ:
def pred(x1, y1):  # возвращает индексы списка
    if x1 < 0 and y1 < 0:
        return 2
    elif x1 < 0 and y1 > 0:
        return 1
    elif x1 > 0 and y1 > 0:
        return 0
    elif x1 > 0 and y1 < 0:
        return 3
    elif x1 == 0 and y1 == 0:  # в центре
        return 4
    elif x1 == 0:              # на оси абсцисс
        return 5
    return 6                   # на оси ординат
list_quarters = ["в 1 четверти",
                 "в 2 четверти",
                 "в 3 четверти",
                 "в 4 четверти",
                 "в начале координат",
                 "на оси абсцисс",
                 "на оси ординат"]

print("Введите координаты точки ")
x = float(input("введите точку x :"))
y = float(input("введите точку y :"))
result = pred(int(x), int(y))
print(f"данная точка находится {list_quarters[result]} ")