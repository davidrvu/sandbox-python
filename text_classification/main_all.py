# DAVIDRVU - 2017

from sklearn import metrics
import argparse
import numpy as np
import pandas as pd
import sys
import tensorflow as tf

sys.path.insert(0, '..//data_science_utils')
from get_dir_file_ext import get_dir_file_ext
from pandas_read_csv import pandas_read_csv
from pandas_write_csv import pandas_write_csv
from split_datasets import split_datasets

# TODOTODO: QUITAR VARIABLES GLOBALES Y REEMPLAZARLAS POR PARAMETROS DE FUNCIONES
EMBEDDING_SIZE = 50
MAX_LABEL = 15
vocab_len = 0

def estimator_spec_for_softmax_classification(logits, labels, mode):
    """Returns EstimatorSpec instance for softmax classification."""
    predicted_classes = tf.argmax(logits, 1)
    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions={'class': predicted_classes, 'prob': tf.nn.softmax(logits)})

    onehot_labels = tf.one_hot(labels, MAX_LABEL, 1, 0)
    loss = tf.losses.softmax_cross_entropy(onehot_labels=onehot_labels, logits=logits)
    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
        train_op    = optimizer.minimize(loss, global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode, loss=loss, train_op=train_op)

    eval_metric_ops = {
            'accuracy': tf.metrics.accuracy(labels=labels, predictions=predicted_classes)
    }
    return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)


#def bag_of_words_model(features, labels, mode, vocab_len): # TODOTODO: ANTES vocab_len era variable GLOBAL
def bag_of_words_model(features, labels, mode): # TODOTODO: ANTES vocab_len era variable GLOBAL
    """A bag-of-words model. Note it disregards the word order in the text."""
    bow_column           = tf.feature_column.categorical_column_with_identity('words', num_buckets=vocab_len)
    bow_embedding_column = tf.feature_column.embedding_column(bow_column, dimension=EMBEDDING_SIZE)
    bow                  = tf.feature_column.input_layer(features, feature_columns=[bow_embedding_column])
    logits               = tf.layers.dense(bow, MAX_LABEL, activation=None)

    return estimator_spec_for_softmax_classification(logits=logits, labels=labels, mode=mode)


#def rnn_model(features, labels, mode, vocab_len):
def rnn_model(features, labels, mode):    
    """RNN model to predict from sequence of words to a class."""
    # Convert indexes of words into embeddings.
    # This creates embeddings matrix of [vocab_len, EMBEDDING_SIZE] and then maps word indexes of the sequence into [batch_size, sequence_length, EMBEDDING_SIZE].
    word_vectors = tf.contrib.layers.embed_sequence(features['words'], vocab_size=vocab_len, embed_dim=EMBEDDING_SIZE)

    # Split into list of embedding per word, while removing doc length dim. word_list results to be a list of tensors [batch_size, EMBEDDING_SIZE].
    word_list = tf.unstack(word_vectors, axis=1)

    # Create a Gated Recurrent Unit cell with hidden size of EMBEDDING_SIZE.
    cell = tf.nn.rnn_cell.GRUCell(EMBEDDING_SIZE)

    # Create an unrolled Recurrent Neural Networks to length of max_vocab_length and passes word_list as inputs for each unit.
    _, encoding = tf.nn.static_rnn(cell, word_list, dtype=tf.float32)

    # Given encoding of RNN, take encoding of last step (e.g hidden size of the neural network of last step) and pass it as features for softmax classification over output classes.
    logits = tf.layers.dense(encoding, MAX_LABEL, activation=None)

    return estimator_spec_for_softmax_classification(logits=logits, labels=labels, mode=mode)


def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~        main all - TEXT CLASSIFICATION    ~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #############################################
    ## ARGUMENTS AND PARAMETERS 
    #############################################
    print("ARGUMENTS AND PARAMETERS: ")
    tf.logging.set_verbosity(tf.logging.INFO)
    parser = argparse.ArgumentParser(description='Process some arguments.')

    parser.add_argument('--debug',   type=int, default=0,  help='a debug flag (for prints)')
    parser.add_argument('--mode',    type=int, default=0,  help='a mode flag') # 0 = rnn text model | 1 = bag_of_words text model
    parser.add_argument('--file_in', type=str, nargs='+',  default=[],   help='input file')

    args = parser.parse_args()

    debug   = args.debug
    mode    = args.mode
    file_in = args.file_in[0]

    print("_________________________________________________________")
    print("debug            = " + str(debug))
    print("mode             = " + str(mode))
    print("file_in          = " + str(file_in))
    print("_________________________________________________________")
    
    ##########################################################################################
    print("\nLoad FULL dataset and split it ... ")
    
    train_perc = 0.89
    split_datasets(file_in, train_perc, "class", final_sort = True)
    [directory, filename_in_base, ext] = get_dir_file_ext(file_in)
    file_train = directory + "//" + filename_in_base + "_train.csv"
    file_test  = directory + "//" + filename_in_base + "_test.csv"

    # SOLO VERIFICACION!!!!!!!!!!! (ALCANZA UN Accuracy ~ 0.73)
    #file_train = directory + "//" + "train_small.csv" 
    #file_test  = directory + "//" + "test_small.csv"

    ##########################################################################################
    print("\nRead train and test datasets ... ")        
    df_train = pandas_read_csv(file_train) 
    df_test  = pandas_read_csv(file_test) 

    x_train  = pd.Series(df_train['content']) # FEATURES
    y_train  = pd.Series(df_train['class'])   # LABELS

    x_test   = pd.Series(df_test['content'])  # FEATURES
    y_test   = pd.Series(df_test['class'])    # LABELS

    print("x_train_size = " + str(x_train.size))
    print("y_train_size = " + str(y_train.size))
    print("x_test_size  = " + str(x_test.size))
    print("y_test_size  = " + str(y_test.size))

    ##########################################################################################
    print("\nProcess vocabulary ...")
    max_vocab_length = 15 # originalmente es 10 -> OJO! Parametro IMPORTANTE! (aumenta % de acierto)
    print("max_vocab_length = " + str(max_vocab_length))
    vocab_processor = tf.contrib.learn.preprocessing.VocabularyProcessor(max_vocab_length)

    x_transform_train = vocab_processor.fit_transform(x_train)
    x_transform_test  = vocab_processor.transform(x_test)

    x_train_vocab = np.array(list(x_transform_train))
    x_test_vocab  = np.array(list(x_transform_test))

    global vocab_len
    vocab_len = len(vocab_processor.vocabulary_) # TODOTODO OJO: ANTES vocab_len ERA VARIABLE GLOBAL
    print("Total words: vocab_len = " + str(vocab_len))

    ##########################################################################################
    print("\nBuild model ...")
    # Switch between rnn_model and bag_of_words_model to test different models.
    if mode == 0:
        model_case = rnn_model
    elif mode == 1:
        # Subtract 1 because:
        # VocabularyProcessor outputs a word-id matrix where word ids start from 1 and 0 means 'no word'. 
        # But categorical_column_with_identity assumes 0-based count and uses -1 for missing word.
        x_train_vocab -= 1
        x_test_vocab  -= 1
        model_case = bag_of_words_model

    classifier = tf.estimator.Estimator(model_fn = model_case)

    ##########################################################################################
    print("\nTraining ...")
    train_input_fn = tf.estimator.inputs.numpy_input_fn(x={'words': x_train_vocab}, y=y_train, batch_size=len(x_train_vocab), num_epochs=None, shuffle=True)
    classifier.train(input_fn=train_input_fn, steps=100)

    ##########################################################################################
    print("\nPredict ...")
    test_input_fn = tf.estimator.inputs.numpy_input_fn(x={'words': x_test_vocab}, y=y_test, num_epochs=1, shuffle=False)

    predictions = classifier.predict(input_fn=test_input_fn)
    y_predicted = np.array(list(p['class'] for p in predictions))
    y_predicted = y_predicted.reshape(np.array(y_test).shape)

    print("y_predicted = ")
    print(y_predicted)

    ##########################################################################################
    print("\nPerformance evaluation ...")

    score = metrics.accuracy_score(y_test, y_predicted)
    print("Accuracy (sklearn): score = " + str(round(score,4)))

    # TODOTODO: OBTENER MATRIZ DE CONFUSIÓN (EN PLOTLY)
    # TODOTODO: OBTENER f1
    # TODOTODO: OBTENER PRECITION
    # TODOTODO: OBTENRE RECALL

    print("DONE!")

if __name__ == "__main__":
        main()