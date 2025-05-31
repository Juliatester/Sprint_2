class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return 0
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return 0            
        else:
            return 101 - place

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return 0
        else:
            return meters * 0.5

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, meters, place):
        place_points = self.get_points_for_place(place)
        meters_points = self.get_points_for_meters(meters)
        total_points = place_points + meters_points
        return total_points

    @staticmethod
    def get_total_points(meters, place):
        place_points = PointsForPlace.get_points_for_place(place)
        meters_points = PointsForMeters.get_points_for_meters(meters)
        total = place_points + meters_points
        return total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10)) 

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))