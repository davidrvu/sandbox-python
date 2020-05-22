# DAVIDRVU - 2020

# LINEAR REGRESSOR BASIC EXAMPLE
# OBJETIVO: Predecir el precio de una vivienda. Features: Superficie y tipo

import tensorflow as tf
import numpy as np
import shutil

def train_input_fn():
    features = {"sq_footage": [   1000,    2000,    3000,   1000,  2000,  3000],
                "type":       ["house", "house", "house",  "apt", "apt", "apt"]}
    labels   =                [    500,    1000,    1500,    700,  1300,  1900]
    return features, labels

def predict_input_fn():
    features = {"sq_footage": [   1500,  1500,    1500,  2500],
                "type":       ["house", "apt", "house", "apt"]}
    return features


def main():
    print("===> LINEAR REGRESSOR BASIC EXAMPLE")

    shutil.rmtree("outdir", ignore_errors= True)

    featcols = [
        tf.feature_column.numeric_column("sq_footage"),
        tf.feature_column.categorical_column_with_vocabulary_list("type", ["house", "apt"])
    ]

    model = tf.estimator.LinearRegressor(featcols, "outdir")

    model.train(train_input_fn, steps = 2000)

    predictions = model.predict(predict_input_fn)

    print(predictions)

    print(next(predictions))
    print(next(predictions))
    print(next(predictions))
    print(next(predictions))

    print("DONE!")

if __name__ == "__main__":
    # execute only if run as a script
    main()