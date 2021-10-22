from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def get_scores(y_pred, y_true):

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    return (accuracy, precision, recall, f1)