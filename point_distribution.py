import random
import numpy as np

class PointDistribution:

    def __init__(self, size, quantity, outlier_prob):
        self.size = size
        self.__points = self.__generate_distribution(quantity)
        self.__outlier_prob = outlier_prob

    # Allows for indexing by the [] operator.
    def __getitem__(self, n):
        return self.__points[n]
    
    # Provides the amount of items available in this container.
    def __len__(self):
        return len(self.__points)

    # Shows a string representation when printing this container.
    def __str__(self) -> str:
        return str(self.__points)

    # Create a point with a uniformly distributed x and y value.
    # Values are bound by the size of this distribution.
    def __generate_point(self):
        x = random.uniform(0, self.size)
        y = random.uniform(0, self.size)
        return (x,y)

    # Generate a quantity of x, y points that fit inside this distribution.
    def __generate_distribution(self, quantity):
        points = [self.__generate_point() for i in range(quantity)]
        return np.array(points)

    # Labels every point in the distribution by their position in the triangle.
    # Creates outliers according to the outlier_prob value.
    def get_labels(self, triangle, outliers=True):
        labels = np.array([self.__get_label(point, triangle) for point in self])
        return labels            

    def __get_label(self, point, triangle):

        is_outlier = random.random() < self.__outlier_prob
        in_triangle = point in triangle
        
        return in_triangle != is_outlier