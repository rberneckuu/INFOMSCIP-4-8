from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def get_scores(data):
    for idx, experiment in enumerate(data):
        y_pred, y_true = experiment

        print("\nPart ", idx + 1)
        print("accuracy score: ", accuracy_score(y_true, y_pred))
        print("precision score: ", precision_score(y_true, y_pred))
        print("recall score: ", recall_score(y_true, y_pred))
        print("f1-score: ", f1_score(y_true, y_pred))