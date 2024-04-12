# 3. Создать класс Point, который представляет собой точку
# в двумерном пространстве.
# Класс должен иметь методы для инициализации координат точки,
# вычисления расстояния до другой точки, а также для получения
# и изменения координат.
class Point:
    def __init__(self, x, y) -> None:
        self.coord_x = x
        self.coord_y = y

    @property
    def coordinates(self) -> tuple:
        return (self.coord_x, self.coord_y)

    @coordinates.setter
    def coordinates(self, new_coords) -> None:
        self.coord_x, self.coord_y = new_coords

    @staticmethod
    def calc_distance(point_a, point_b) -> float:
        delta_x_pif = (point_a.coord_x - point_b.coord_x) ** 2
        delta_y_pif = (point_a.coord_y - point_b.coord_y) ** 2
        return (delta_x_pif + delta_y_pif) ** 0.5


if __name__ == "__main__":
    point1 = Point(2, 6)
    point2 = Point(4, 4)
    print("Координаты точки 1:", point1.coordinates)
    print("Координаты точки 2:", point2.coordinates)
    distance = Point.calc_distance(point1, point2)
    print("Расстояние между точкой 1 и точкой 2:", distance)
    point2.coordinates = (10, 10)
    print("Новые координаты точки 2:", point2.coordinates)
    distance_new = Point.calc_distance(point1, point2)
    print("Расстояние между точкой 1 и точкой 2:", distance_new)
