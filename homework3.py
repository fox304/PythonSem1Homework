# Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти четверти,
#  в которой находится эта точка (или на какой оси она находится).

# Первый способ:

print("Введите координаты точки ")
x = int(input("введите точку x :"))
y = int(input("введите точку y :"))

if x == y == 0:
    print("ваша точка находится в начале координат")
elif x == 0:
    print("ваша точка находится на оси абсцисс")
elif y == 0:
    print("ваша точка находится на оси ординат")

elif x > 0 and y > 0:
    print("ваша точка находится в первой четверти")

elif x > 0 and y < 0:
    print("ваша точка находится в четвёртой четверти")

elif x < 0 and y > 0:
    print("ваша точка находится в второй четверти")

else:
    print("ваша точка находится в третьей четверти") 
      