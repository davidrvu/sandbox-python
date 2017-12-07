# DAVIDRVU - 2017
from confusion_plotly import confusion_plotly
from sklearn import metrics

class performance_struct:
    def __init__(self):
        self.avg_precision_score = 0.0
        self.avg_recall_score    = 0.0
        self.avg_f1_score        = 0.0
        self.acc_score           = 0.0

def classification_algorithm_performance(y_test, y_predicted, figure_name, dictionary_labels, unique_labels):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nCLASSIFICATION-ALGORITHM PERFORMANCE: ")

    classif_report = metrics.classification_report(y_test, y_predicted)
    print("\nclassif_report = ")
    print(classif_report)

    avg_precision_score = round(metrics.precision_score(y_test, y_predicted, average="macro"),3)
    avg_recall_score    = round(metrics.recall_score(y_test, y_predicted,    average="macro"),3)
    avg_f1_score        = round(metrics.f1_score(y_test, y_predicted,        average="macro"),3)

    print("avg_precision_score = " + str(avg_precision_score))
    print("avg_recall_score    = " + str(avg_recall_score))
    print("avg_f1_score        = " + str(avg_f1_score))

    conf_matrix = metrics.confusion_matrix(y_test, y_predicted)
    print("\nconfusion_matrix  = ")
    print(conf_matrix) # conf_matrix: Lista de listas

    acc_score = round(metrics.accuracy_score(y_test, y_predicted),3)
    print("\naccuracy_score = " + str(acc_score))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    algo_performance = performance_struct()
    algo_performance.avg_precision_score = avg_precision_score
    algo_performance.avg_recall_score    = avg_recall_score
    algo_performance.avg_f1_score        = avg_f1_score
    algo_performance.acc_score           = acc_score

    confusion_plotly(conf_matrix, algo_performance, figure_name, dictionary_labels, unique_labels)