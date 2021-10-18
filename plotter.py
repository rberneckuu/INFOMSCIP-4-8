import matplotlib.pyplot as plt

class ClassificationPlotter:

    def __init__(self, distribution, triangle):
        self.__distribution = distribution
        self.__triangle = triangle

    def show(self):
        self.__plot_triangle()
        self.__plot_points()

        size = self.__distribution.size
        plt.axis([0, size, 0, size])
        plt.title("k-NN classification")

        plt.show()

    def __plot_points(self):
        x, y = self.__distribution.get_x_y()
        labels = self.__distribution.label_points(self.__triangle)
        plt.scatter(x, y, c=labels)


    def __plot_triangle(self):

        points = self.__triangle.points
        triangle = plt.Polygon(points, edgecolor="black", facecolor="None")
        plt.gca().add_patch(triangle)