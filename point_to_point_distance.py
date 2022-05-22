from math import sqrt


def get_distance(x1, y1, x2, y2):
    term_1 = (x1 ** 2 - x2 ** 2)
    term_2 = (y1 ** 2 - y2 ** 2)
    return sqrt(term_1**2 + term_2**2)


points = input('enter the to points ').split()

[point1, point2] = points
point1 = point1.split(',')
point2 = point2.split(',')
distance = get_distance(float(point1[0]), float(point1[1]), float(point2[0]), float(point2[1]))

print(f'The distance between the two points is {distance}')
