class Triangle:

    def __init__(self, points):
        self.points = points


    def __contains__(self, scatter_point):
        v1, v2, v3 = self.points     
        d1 = self.__sign_point(scatter_point, v1, v2)
        d2 = self.__sign_point(scatter_point, v2, v3)
        d3 = self.__sign_point(scatter_point, v3, v1)
        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
        print(not(has_neg and has_pos))

    def __sign_point(self, p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])