import numpy as np
from point_distribution import PointDistribution
from triangle import Triangle

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# INITIALIZE CONSTANTS
# 
# BASE EXPERIMENT PARAMETERS
FIELD_SIZE = 10
NUM_TEST_POINTS = 10000

NUM_POINTS = 500
OUTLIER_PROB = 0
NUM_NEIGHBORS = 5
BASIC_TRIANGLE = Triangle([[3,3], [7,3], [7,7]])

# ALTERNATIVE EXPERIMENT PARAMETERS
EXP1_NUM_POINTS = [100, 200, 300, 400, 500, 600, 700, 800]
EXP2_OUTLIER_PROB = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]

# All triangles should have the same area.
EXP3_TRIANGLES = [
    # Normal triangles.
    # Top in the middle, right, and far right.
    Triangle([[3,3], [7,3], [5,7]]),
    BASIC_TRIANGLE,
    Triangle([[3,3], [7,3], [9,7]]),
    
    # Elongated triangles
    # Top in the middle, right, and far right.
    Triangle([[4,1], [6,1], [5, 9]]),
    Triangle([[4,1], [6,1], [7, 9]]),
    Triangle([[4,1], [6,1], [9, 9]]),

    # Flat triangle
    # Top in the middle, and right.
    Triangle([[1,4], [9,4], [5,6]]),
    Triangle([[1,4], [9,4], [7,6]])
]

def run_experiment(num_points=NUM_POINTS, outlier_prob=OUTLIER_PROB, num_neighbors=NUM_NEIGHBORS, triangle=BASIC_TRIANGLE):

    # Generate a distribution with labels.
    distribution = PointDistribution(FIELD_SIZE, num_points, outlier_prob)
    labels = distribution.get_labels(triangle)

    # Fit k-neirest neighbor classifier on our generated distribution
    knn = KNeighborsClassifier(n_neighbors=num_neighbors)
    knn.fit(distribution, labels)

    # Generate test distribution with labels, and predict test points.
    test_distribution = PointDistribution(FIELD_SIZE, NUM_TEST_POINTS, OUTLIER_PROB)
    true_labels = test_distribution.get_labels(triangle)
    pred_labels = knn.predict(test_distribution)

    return pred_labels, true_labels

# Run a generic experiment, altering one variable while keeping the others the same.
def run_experiments(alternative_variables, variable_key):

    # Prepare data storage.
    shape = (len(alternative_variables), 2, NUM_TEST_POINTS)
    data = np.ndarray(shape, dtype=bool)

    # Loop over all alternative variables and run an experiment with them.
    for idx, variable in enumerate(alternative_variables):

        # Put the key and variable in a dictionary, then unpack it to pass the keyword parameter.
        # Get the predicted labels, along with the true labels.
        pred_labels, true_labels = run_experiment(**{variable_key: variable})
        data[idx] = (pred_labels, true_labels)

    return data

# Generates data for experiment one. Alternates the num_points variable.
def experiment_1():
    return run_experiments(EXP1_NUM_POINTS, "num_points")

# Generates data for experiment two. Alternates the outlier probability variable.
def experiment_2():
    return run_experiments(EXP2_OUTLIER_PROB, "outlier_prob")

# Generates data for experiment three. Alternates the triangle (shape) variable.
def experiment_3():
    return run_experiments(EXP3_TRIANGLES, "triangle")

