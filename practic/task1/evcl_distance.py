import math


def eucl_dist(point1, point2):
    if len(point1) != len(point2):
        raise ValueError("Размерность точек должна быть одинаковой")

    squa_diff = [(point1[i] - point2[i]) ** 2 for i in range(len(point1))]

    sum_squa_diff = sum(squa_diff)

    distance = math.sqrt(sum_squa_diff)
    return distance


# Пример использования функции
point1 = [1, 2, 3]
point2 = [4, 5, 6]
distance = eucl_dist(point1, point2)
print("Евклидово расстояние между точкой 1 и точкой 2:", distance)
