import matplotlib.pyplot as plt
from matplotlib import cm

class ClassificationPlotter:

    def __init__(self, distribution, triangle, labels):
        self.__distribution = distribution
        self.__triangle = triangle
        self.__labels = labels

    def show(self):
        self.__plot_triangle()
        self.__plot_points()

        size = self.__distribution.size
        plt.axis([0, size, 0, size])
        plt.title("k-NN classification")

        plt.show()

    def __plot_points(self):
        x, y = self.__distribution.get_x_y()
        
        colormap = cm.get_cmap('coolwarm')
        plt.scatter(x, y, c=self.__labels, cmap=colormap)


    def __plot_triangle(self):

        points = self.__triangle.points
        triangle = plt.Polygon(points, edgecolor="black", facecolor="None")
        plt.gca().add_patch(triangle)