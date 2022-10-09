# Напишите программу,
#  которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
"""
   y
    |            (x1-x2)
    |       @-------------------------
    |    (x1,y1)                     |
    |                                | (y1-y2)
    |                                |
    |                                |
    |                                @
    |                            (x2,y2)
    |
    ---------------------------------------------------- x


"""

# поскольку значения (x1-x2) и (y1-y2) возводятся в квадрат , то неважно какой у них знак

x1 = int(input("введите значение первой точки x1"))
y1 = int(input("введите значение первой точки y1"))
x2 = int(input("введите значение второй точки x2"))
y2 = int(input("введите значение второй точки y2"))
z1 = (x1 - x2)**2
z2 = (y1 - y2)**2
print(f"расстояние между точками ({x1},{y1}) и ({x2},{y2}) будет равно {(z1 + z2)**0.5}")


