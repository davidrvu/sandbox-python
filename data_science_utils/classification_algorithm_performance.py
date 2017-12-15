# DAVIDRVU - 2017

from confusion_plotly import confusion_plotly
from histogram_train_test_results import histogram_train_test_results
from sklearn import metrics

class performance_struct:
    def __init__(self):
        self.avg_precision_score = 0.0
        self.avg_recall_score    = 0.0
        self.avg_f1_score        = 0.0
        self.acc_score           = 0.0

def classification_algorithm_performance(train_set_counts, y_test, y_predicted, confusion_fig_name, histogram_fig_name, dictionary_labels, unique_labels):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nCLASSIFICATION-ALGORITHM PERFORMANCE: ")

    classif_report = metrics.classification_report(y_test, y_predicted)
    print("\nclassif_report = ")
    print(classif_report)

    avg_precision_score = round(metrics.precision_score(y_test, y_predicted, average="macro"),3) # precision = tp / (tp + fp)
    avg_recall_score    = round(metrics.recall_score(y_test, y_predicted,    average="macro"),3) # recall    = tp / (tp + fn)
    avg_f1_score        = round(metrics.f1_score(y_test, y_predicted,        average="macro"),3) # f1 = 2 * (precision * recall) / (precision + recall)

    print("avg_precision_score = " + str(avg_precision_score))
    print("avg_recall_score    = " + str(avg_recall_score))
    print("avg_f1_score        = " + str(avg_f1_score))

    conf_matrix = metrics.confusion_matrix(y_test, y_predicted)
    print("\nconfusion_matrix  = ")
    print(conf_matrix) # conf_matrix: Lista de listas

    test_correct       = conf_matrix.diagonal()
    test_incorrect     = conf_matrix.sum(axis=1) - test_correct
    accuracy_per_class = conf_matrix.diagonal()/conf_matrix.sum(axis=1)

    print("\naccuracy_per_class = ")
    print(accuracy_per_class)

    acc_score = round(metrics.accuracy_score(y_test, y_predicted),3)
    print("\naccuracy_score = " + str(acc_score))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    algo_performance = performance_struct()
    algo_performance.avg_precision_score = avg_precision_score
    algo_performance.avg_recall_score    = avg_recall_score
    algo_performance.avg_f1_score        = avg_f1_score
    algo_performance.acc_score           = acc_score

    confusion_plotly(conf_matrix, algo_performance, confusion_fig_name, dictionary_labels, unique_labels, accuracy_per_class)
    histogram_train_test_results(algo_performance, train_set_counts, test_correct, test_incorrect, histogram_fig_name, dictionary_labels, unique_labels, accuracy_per_class, "h")