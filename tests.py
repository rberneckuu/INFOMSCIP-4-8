import math
import numpy
from experiments import BASIC_TRIANGLE, EXP3_TRIANGLES
from plotter import ClassificationPlotter
from point_distribution import PointDistribution

from triangle import Triangle

def test_distribution():
    
    points = PointDistribution(10, 100, 0.05)
    labels = points.get_labels(BASIC_TRIANGLE)
    plotter = ClassificationPlotter(points, BASIC_TRIANGLE, labels)
    plotter.show()

# Check whether every test triangle has the same area.
# We expect horizontal triangle bases.
def test_triangle_areas(triangles):
    areas = []

    for triangle in triangles:

        # Calculate area and add to list.
        area = triangle.get_area()
        areas.append(area)
    
    # If there were triangles with distinct areas, the set will have a length > 1.
    areas = set(areas)
    
    if len(areas) == 1:
        print("Every triangle has the same area.")
    else:
        raise Exception("The test set for experiment 3 contains triangles with distinct areas.")

def test_triangle_perimeters(triangles):

    perimeters = []
    for triangle in triangles:
        perimeter = triangle.get_perimeter()
        perimeters.append(perimeter)

    perimeters_sorted = numpy.sort(perimeters)
    diffs = {}
    idx = 0

    while idx + 1 < len(perimeters):
        perim_1, perim_2 = perimeters_sorted[idx:idx + 2]
        diff = perim_2 - perim_1
        diffs[f"{idx + 1}-{idx + 2}"] = diff
        idx += 1


    print("Perimeter sorting", numpy.argsort(perimeters))
    print("Sorted perimeters", perimeters_sorted)
    print("Perimeter differences", diffs)

# All triangles should have the same area.
test_distribution()
test_triangle_perimeters(EXP3_TRIANGLES)
test_triangle_areas(EXP3_TRIANGLES)
ClassificationPlotter.plot_triangles(EXP3_TRIANGLES)