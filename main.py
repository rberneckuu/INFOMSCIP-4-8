from points import Points
import matplotlib.pyplot as plt
import numpy as np

def main():
    """ Main program """ 

    points = Points(10, 10)
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    tri_coordinates = np.array([[3,3], [7,3], [7, 7]])
    triangle = plt.Polygon(tri_coordinates, edgecolor="black", facecolor="None")
    plt.gca().add_patch(triangle)

    plt.scatter(x, y)
    plt.axis([0, 10, 0, 10])
    plt.title("k-NN classification")
  

    plt.show()
    return 0

if __name__ == "__main__":
    main()