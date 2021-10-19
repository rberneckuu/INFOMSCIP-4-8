import random
import numpy as np
class PointDistribution:

    def __init__(self, size, quantity, outlier_prob):
        self.size = size
        self.__points = self.__generate_distribution(quantity)
        self.__outlier_prob = outlier_prob

    def __getitem__(self, n):
        return self.__points[n]
    
    def __len__(self):
        return len(self.__points)

    def __str__(self) -> str:
        return str(self.__points)

    def __generate_point(self):
        x = random.uniform(0, self.size)
        y = random.uniform(0, self.size)
        return (x,y)

    def __generate_distribution(self, quantity):
        points = [self.__generate_point() for i in range(quantity)]
        return np.array(points)

    def get_x_y(self):
        x = [point[0] for point in self]
        y = [point[1] for point in self]
        return x, y

    def get_labels(self, triangle):
        labels = np.array([self.__get_label(point, triangle) for point in self])
        return labels            

    def __get_label(self, point, triangle):

        is_outlier = random.random() < self.__outlier_prob
        in_triangle = point in triangle
        
        return in_triangle != is_outlier