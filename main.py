from point_distribution import PointDistribution

from triangle import Triangle
from plotter import ClassificationPlotter
import matplotlib.pyplot as plt
import numpy as np

def main():
    """ Main program """ 

    points = PointDistribution(10, 100, 0)
    triangle = Triangle([[3,3], [7,3], [7,7]])
    
    plotter = ClassificationPlotter(points, triangle)
    plotter.show()
    return 0

if __name__ == "__main__":
    main()