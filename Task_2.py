# Задача 2.	Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = [True, False]
Y = [True, False]
Z = [True, False]

for x in X:
    for y in Y:
        for z in Z:
            if not(x or y or z) == (not x) and (not y) and (not z):
                print(True)
            else:
                print(False)     