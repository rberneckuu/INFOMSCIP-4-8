import math
from itertools import combinations
class Triangle:

    def __init__(self, points):
        self.__points = points

    def __getitem__(self, n):
        return self.__points[n]

    def __len__(self):
        return len(self.__points)

    # Determines whether a point is inside the triangle.
    def __contains__(self, test_point):
        v1, v2, v3 = self.__points
        d1 = self.__sign_point(test_point, v1, v2)
        d2 = self.__sign_point(test_point, v2, v3)
        d3 = self.__sign_point(test_point, v3, v1)

        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
        
        return not (has_neg and has_pos)

    def __sign_point(self, p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    def get_area(self):
        # Get all triangle vertices.
        v1, v2, v3 = self
        
        # Get relevant x and y points.
        x1, y1 = v1
        x2 = v2[0]
        y2 = v3[1]
        
        # Calculate base and height.
        base = x2 - x1
        height = y2 - y1

        # Calculate area and add to list.
        area = 0.5 * base * height
        return area

    def get_perimeter(self):
        vertex_pairs = combinations([0, 1, 2], 2)
        distances = []

        for pair in vertex_pairs:
            v1 = self[pair[0]]
            v2 = self[pair[1]]
        
            # Get distance between points
            distance = math.sqrt( ((v1[0]-v2[0])**2)+((v1[1]-v2[1])**2))
            distances.append(distance)
        
        perimeter = sum(distances)
        
        return perimeter