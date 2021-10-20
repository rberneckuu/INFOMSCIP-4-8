from experiments import experiment_1, experiment_2, experiment_3
from analysis import get_scores

def main():
    """ Main program """
    
    print("\n######## RUNNING EXPERIMENT 1")
    exp1_data = experiment_1()
    get_scores(exp1_data)

    print("\n######## RUNNING EXPERIMENT 2")
    exp2_data = experiment_2()
    get_scores(exp2_data)

    print("\n######## RUNNING EXPERIMENT 3")
    exp3_data = experiment_3()
    get_scores(exp3_data)

    return 0

if __name__ == "__main__":
    main()