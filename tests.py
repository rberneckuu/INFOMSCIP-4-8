from experiments import EXP3_TRIANGLES

# Check whether every test triangle has the same area.
# We expect horizontal triangle bases.
def test_triangle_areas():
    areas = []

    for triangle in EXP3_TRIANGLES:

        # Get all triangle vertices.
        v1, v2, v3 = triangle
        
        # Get relevant x and y points.
        x1, y1 = v1
        x2 = v2[0]
        y2 = v3[1]
        
        # Calculate base and height.
        base = x2 - x1
        height = y2 - y1

        # Calculate area and add to list.
        area = 0.5 * base * height
        areas.append(area)
    
    # If there were triangles with distinct areas, the set will have a length > 1.
    areas = set(areas)
    
    if len(areas) == 1:
        print("Every triangle has the same area.")
    else:
        raise Exception("The test set for experiment 3 contains triangles with distinct areas.")