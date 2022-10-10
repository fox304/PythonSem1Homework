# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным

list_of_weekdays = ["Mondey","Tuesday","Wednesday","Thurthday","Friday","Saturday","Sunday"]
number_of_weekday = input("Введите номер дня недели (от 1 до 7) ")
#  в while запрет на ввод данных , отличных от цифр 1,2,3,4,5,6,7
while len(number_of_weekday) > 1 or not (48 < ord(number_of_weekday) < 56):  
    number_of_weekday = input("Советую всё-таки ввести цифру от 1 до 7 , иначе день пролетит незаметно ")
if int(number_of_weekday) < 6:
    yes_or_not = "НЕ"
else:
    yes_or_not = ""
print("{0}  {1} является  выходным днём".format(list_of_weekdays[int(number_of_weekday)-1],yes_or_not))