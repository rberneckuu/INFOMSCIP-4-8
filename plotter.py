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
        x = [point[0] for point in self.__distribution]
        y = [point[1] for point in self.__distribution]
        
        colormap = cm.get_cmap('coolwarm')
        plt.scatter(x, y, c=self.__labels, cmap=colormap)


    def __plot_triangle(self):

        points = self.__triangle
        triangle = plt.Polygon(points, edgecolor="black", facecolor="None")
        plt.gca().add_patch(triangle)

    @classmethod
    def plot_triangles(cls, triangles):
        
        # Prepare vertex labels.
        point_names = ['A', 'B', 'C']
        point_offsets = [[-0.5, -0.75],[-0.5, -0.75],[0, 0.35]]

        for idx, triangle in enumerate(triangles):
            tri_number = idx + 1

            for idy, point in enumerate(triangle):
                x, y = point

                # Get text position
                offset_x, offset_y = point_offsets[idy]
                text_x, text_y = (x + offset_x, y + offset_y)
                
                # Add text to the plot for the triangle point.
                point_name = point_names[idy]
                plt.text(text_x, text_y, f"{point_name}: ({x}, {y})")
            
            # Add the triangle to the plot
            poly = plt.Polygon(triangle, edgecolor="black", facecolor="None")
            plt.gca().add_patch(poly)

            plt.suptitle(f"Triangle {tri_number}")

            # Calculate perimeter for the subtitle.
            perimeter = triangle.get_perimeter()
            perimeter = round(perimeter, 2)
            plt.title(f"Perimeter ≈ {perimeter}", fontsize=10)

            # Set the size of the plot, then hide the axes.
            plt.axis([0, 10, 0, 10])
            plt.axis('off')

            # Save and show the plot.
            plt.savefig(f"./exports/triangle-{tri_number}.png", bbox_inches="tight")
            plt.show()