# # Напишите программу, которая по заданному номеру четверти
# показывает диапазон возможных координат точек в этой четверти (x и y).
num_quarter = int(input())
if num_quarter == 1:
    print(f"диапазон возможных координат  точек (x,y) в {num_quarter} четверти :\n\
         X от нуля до бесконечности,Y от нуля до бесконечности")

elif num_quarter == 2:
    print(f"диапазон возможных координат  точек (x,y) в {num_quarter} четверти :\n\
         X от нуля до минус бесконечности,Y от нуля до бесконечности")

elif num_quarter == 3:
    print(f"диапазон возможных координат  точек (x,y) в {num_quarter} четверти :\n\
         X от нуля до минус бесконечности,Y от нуля до минус бесконечности")

elif num_quarter == 4:
    print(f"диапазон возможных координат  точек (x,y) в {num_quarter} четверти :\n\
            X от нуля до бесконечности,Y от нуля до минус бесконечности")

else:
    print("Такой четверти нет ")
    