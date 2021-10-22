from experiments import experiment_1, experiment_2, experiment_3

import pandas as pd

def main():
    """ Main program """
    writer = pd.ExcelWriter(f".\exports\experiments.xlsx")

    scores1 = experiment_1()
    scores2 = experiment_2()
    scores3 = experiment_3()

    scores1.to_excel(sheet_name="Experiment 1", excel_writer=writer)
    scores2.to_excel(sheet_name="Experiment 2", excel_writer=writer)
    scores3.to_excel(sheet_name="Experiment 3", excel_writer=writer)
    writer.close()
    
    return 0

if __name__ == "__main__":
    main()