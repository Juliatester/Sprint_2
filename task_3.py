class PointsForPlace:
    points = 0
    
    @classmethod
    def get_points_for_place(cls, place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            cls.points = 0
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            cls.points = 0
        else:
            cls.points = 101 - place
        return cls.points


class PointsForMeters:
    points = 0
    
    @classmethod
    def get_points_for_meters(cls, meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            cls.points = 0
        else:
            cls.points = meters * 0.5
        return cls.points


class TotalPoints(PointsForPlace, PointsForMeters):
    total = 0
    
    @classmethod
    def get_total_points(cls, meters, place):
        place_points = cls.get_points_for_place(place)
        meters_points = cls.get_points_for_meters(meters)
        cls.total = place_points + meters_points
        return cls.total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))