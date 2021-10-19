from point_distribution import PointDistribution

from triangle import Triangle
from plotter import ClassificationPlotter
import matplotlib.pyplot as plt
import numpy as np

from sklearn.neighbors import KNeighborsClassifier

def main():
    """ Main program """ 

    points = PointDistribution(10, 100, 0.01)
    triangle = Triangle([[3,3], [7,3], [7,7]])
    labels = points.get_labels(triangle)
    
    plotter = ClassificationPlotter(points, triangle, labels)
    
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(points, labels)
    
    plotter.show()
    return 0

if __name__ == "__main__":
    main()