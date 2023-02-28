import math
x1 = float(input("Введiть координату x1 точки A: "))
y1 = float(input("Введiть координату y1 точки A: "))
x2 = float(input("Введiть координату x2 точки B: "))
y2 = float(input("Введiть координату y2 точки B: "))

angle_a = math.atan2(y1, x1)
angle_b = math.atan2(y2, x2)

if angle_a > angle_b:
    print("Вiдрiзок OA утворює бiльший кут з вiссю ОХ.")
else:
    print("Вiдрiзок OB утворює бiльший кут з вiссю ОХ.")
