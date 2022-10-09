# Задача 4.	Напишите программу, которая по заданному номеру четверти, показывает диапазон
#           возможных координат точек в этой четверти (x и y).

quarter_number = int(input("Введите номер четверти плоскости: "))

if quarter_number == 1:
    print('Диапозон координат: \nХ = от > 0 до inf \nY = от > 0 до inf')
elif quarter_number == 2:
    print('Диапозон координат: \nХ = от < 0 до -inf \nY = от > 0 до inf')
elif quarter_number == 3:
    print('Диапозон координат: \nХ = от < 0 до -inf \nY = от < 0 до -inf')
elif quarter_number == 4:
    print('Диапозон координат: \nХ = от > 0 до inf \nY = от < 0 до -inf')
