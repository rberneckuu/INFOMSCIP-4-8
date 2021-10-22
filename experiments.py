import numpy as np
import xarray as xr
from point_distribution import PointDistribution
from triangle import Triangle

from sklearn.neighbors import KNeighborsClassifier
from analysis import get_scores

# INITIALIZE CONSTANTS
# 
# BASE EXPERIMENT PARAMETERS
TEST_RUNS = 20
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

    # Prepare experiment labels for the eventual export to excel.
    experiment_labels = [f"Case {i + 1}" for i in range(len(alternative_variables))]
    score_labels = [f"Accuracy", "Precision", "Recall", "F1"]
    run_labels = [f"Run {i + 1}" for i in range(TEST_RUNS)]
    
    # Prepare data storage.
    data = []

    # Case, Score, run
    # Loop over all alternative variables and run an experiment with them.
    for idx, variable in enumerate(alternative_variables):
        print(f"Starting case {idx + 1} with {variable_key} = {variable}")

        # 4 lists for accuracy, precision, recall and f1 scores.
        score_runs = [[], [], [], []]

        for run in range(TEST_RUNS):
            print(f"Run {run + 1}")

            # Put the key and variable in a dictionary, then unpack it to pass the keyword parameter.
            # Get the predicted labels, along with the true labels.
            pred_labels, true_labels = run_experiment(**{variable_key: variable})
            scores = get_scores(pred_labels, true_labels)

            # Assign each score to its respective list for this run.
            for idy, score in enumerate(scores):
                score_runs[idy].append(score)

        data.append(score_runs)
    
    # Prepare the data as an array.
    experiment_data = np.asarray(data)

    # 3D Xarray for storing labeled data.
    xarr = xr.DataArray(
        data=experiment_data, 
        dims=["Cases", "Scores", "Runs"],
        coords=dict(
            Cases=experiment_labels,
            Scores=score_labels,
            Runs=run_labels
        )
    )

    # Series can be exported to excel.
    series = xarr.to_series()
    return series

# Generates data for experiment one. Alternates the num_points variable.
def experiment_1():
    return run_experiments(EXP1_NUM_POINTS, "num_points")

# Generates data for experiment two. Alternates the outlier probability variable.
def experiment_2():
    return run_experiments(EXP2_OUTLIER_PROB, "outlier_prob")

# Generates data for experiment three. Alternates the triangle (shape) variable.
def experiment_3():
    return run_experiments(EXP3_TRIANGLES, "triangle")

