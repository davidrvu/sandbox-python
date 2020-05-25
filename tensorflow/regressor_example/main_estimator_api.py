# DAVIDRVU - 2020

import tensorflow as tf
import pandas as pd
import numpy as np
import shutil
import itertools
import os

print(tf.__version__)

# In CSV, label is the first column, after the features, followed by the key
CSV_COLUMNS = ['fare_amount', 'pickuplon','pickuplat','dropofflon','dropofflat','passengers', 'key']
FEATURES    = CSV_COLUMNS[1:len(CSV_COLUMNS) - 1]
LABEL       = CSV_COLUMNS[0]

def make_input_fn(df, num_epochs):
  return tf.estimator.inputs.pandas_input_fn(
    x = df,
    y = df[LABEL],
    batch_size = 128,
    num_epochs = num_epochs,
    shuffle = True,
    queue_capacity = 1000,
    num_threads = 1
  )

def make_feature_cols():
    input_columns = [tf.feature_column.numeric_column(k) for k in FEATURES]
    return input_columns

def print_rmse(model, df):
  metrics = model.evaluate(input_fn = make_input_fn(df, num_epochs = 10))
  print('RMSE on dataset = {}'.format(np.sqrt(metrics['average_loss'])))

def main():
    script_path = os.path.dirname(os.path.realpath(__file__))
    df_train = pd.read_csv(os.path.join(script_path, 'input', 'taxi-train.csv'), header = None, names = CSV_COLUMNS)
    df_valid = pd.read_csv(os.path.join(script_path, 'input', 'taxi-valid.csv'), header = None, names = CSV_COLUMNS)
    df_test  = pd.read_csv(os.path.join(script_path, 'input', 'taxi-test.csv' ), header = None, names = CSV_COLUMNS)

    tf.logging.set_verbosity(tf.logging.INFO)

    OUTDIR = 'taxi_trained'
    shutil.rmtree(OUTDIR, ignore_errors = True) # start fresh each time

    model = tf.estimator.LinearRegressor(feature_columns = make_feature_cols(), model_dir = OUTDIR)

    model.train(input_fn = make_input_fn(df_train, num_epochs = 10))

    print_rmse(model, df_valid)

    # Read saved model and use it for prediction
    model = tf.estimator.LinearRegressor(
            feature_columns = make_feature_cols(),
            model_dir = OUTDIR
    )
    preds_iter = model.predict(input_fn = make_input_fn(df_valid, 1))
    print([pred['predictions'][0] for pred in list(itertools.islice(preds_iter, 5))])

    #####################################################################################
    # Deep Neural Network regression 
    #####################################################################################
    print("\nDeep Neural Network regression...")
    tf.logging.set_verbosity(tf.logging.INFO)
    shutil.rmtree(OUTDIR, ignore_errors = True) # Start fresh each time
    model = tf.estimator.DNNRegressor(
                                        hidden_units = [32, 8, 2],
                                        feature_columns = make_feature_cols(),
                                        model_dir = OUTDIR
                                     )
    model.train(input_fn = make_input_fn(df_train, num_epochs = 100))
    print_rmse(model, df_valid)

    print("DONE!")

if __name__ == "__main__":
    main()