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

def estimator_spec_for_softmax_classification(logits, labels, mode, params):
    """Returns EstimatorSpec instance for softmax classification."""
    predicted_classes = tf.argmax(logits, 1)
    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions={'class': predicted_classes, 'prob': tf.nn.softmax(logits)})

    onehot_labels = tf.one_hot(labels, params['max_label'], 1, 0)
    loss = tf.losses.softmax_cross_entropy(onehot_labels=onehot_labels, logits=logits)
    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
        train_op    = optimizer.minimize(loss, global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode, loss=loss, train_op=train_op)

    eval_metric_ops = {
            'accuracy': tf.metrics.accuracy(labels=labels, predictions=predicted_classes)
    }
    return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)

def bag_of_words_model(features, labels, mode, params):
    """A bag-of-words model. Note it disregards the word order in the text."""
    bow_column           = tf.feature_column.categorical_column_with_identity('words', num_buckets=params['vocab_len'])
    bow_embedding_column = tf.feature_column.embedding_column(bow_column, dimension=params['embedding_size'])   
    bow                  = tf.feature_column.input_layer(features, feature_columns=[bow_embedding_column])
    logits               = tf.layers.dense(bow, params['max_label'], activation=None)

    return estimator_spec_for_softmax_classification(logits=logits, labels=labels, mode=mode, params=params)

def rnn_model(features, labels, mode, params):    
    """RNN model to predict from sequence of words to a class."""
    # Convert indexes of words into embeddings.
    # This creates embeddings matrix of [vocab_len, embedding_size] and then maps word indexes of the sequence into [batch_size, sequence_length, embedding_size].
    word_vectors = tf.contrib.layers.embed_sequence(features['words'], vocab_size=params['vocab_len'], embed_dim=params['embedding_size'])

    # Split into list of embedding per word, while removing doc length dim. word_list results to be a list of tensors [batch_size, embedding_size].
    word_list = tf.unstack(word_vectors, axis=1)

    # Create a Gated Recurrent Unit cell with hidden size of embedding_size.
    cell = tf.nn.rnn_cell.GRUCell(params['embedding_size'])

    # Create an unrolled Recurrent Neural Networks to length of max_vocab_length and passes word_list as inputs for each unit.
    _, encoding = tf.nn.static_rnn(cell, word_list, dtype=tf.float32)

    # Given encoding of RNN, take encoding of last step (e.g hidden size of the neural network of last step) and pass it as features for softmax classification over output classes.
    logits = tf.layers.dense(encoding, params['max_label'], activation=None)

    return estimator_spec_for_softmax_classification(logits=logits, labels=labels, mode=mode, params=params)


def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~        main all - TEXT CLASSIFICATION    ~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #############################################
    ## ARGUMENTS 
    #############################################
    print("ARGUMENTS AND PARAMETERS: ")
    tf.logging.set_verbosity(tf.logging.INFO)
    parser = argparse.ArgumentParser(description='Process some arguments.')

    parser.add_argument('--debug',            type=int,             default=0,    help='a debug flag (for prints)')
    parser.add_argument('--model_mode',       type=int,             default=0,    help='a model_mode flag') # 0 = rnn text model | 1 = bag_of_words text model
    parser.add_argument('--file_in',          type=str, nargs='+',  default=[],   help='input file')
    parser.add_argument('--train_perc',       type=float,           default=0.89, help='train set percentage')
    parser.add_argument('--max_vocab_length', type=int,             default=15,   help='max vocabulary length')
    parser.add_argument('--embedding_size',   type=int,             default=50,   help='embedding size')

    args = parser.parse_args()

    debug            = args.debug
    model_mode       = args.model_mode
    file_in          = args.file_in[0]
    train_perc       = args.train_perc
    max_vocab_length = args.max_vocab_length
    embedding_size   = args.embedding_size

    print("_________________________________________________________")
    print("_________________ARGUMENTS_______________________________")
    print("debug            = " + str(debug))
    print("model_mode       = " + str(model_mode))
    print("file_in          = " + str(file_in))
    print("train_perc       = " + str(train_perc))
    print("max_vocab_length = " + str(max_vocab_length))
    print("embedding_size   = " + str(embedding_size))
    print("_________________________________________________________")
    
    ##########################################################################################
    print("\nLoad FULL dataset and split it ... ")
    
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

    unique_labels_train = set(y_train.as_matrix())
    unique_labels_test  = set(y_test.as_matrix())
    unique_labels       = list(set(list(unique_labels_train) + list(unique_labels_test)))
    unique_labels.sort() # SOLO FUNCIONARÁ EN CASO DE labels STRING
    unique_labels_len   = len(unique_labels)
    print(unique_labels)
    print("unique_labels = ")
    print(unique_labels)
    print("unique_labels_len = " + str(unique_labels_len))
    max_label = unique_labels_len + 1
    print("max_label         = " + str(max_label))

    ##########################################################################################
    # LABELS from STRING to INTEGER
    y_train_type = y_train.dtype
    y_test_type  = y_test.dtype
    print("y_train_type = " + str(y_train_type))
    print("y_test_type  = " + str(y_test_type))
    dictionary_label_flag = 0
    if (y_train_type == "object" or y_test_type == "object"):
        dictionary_label_flag = 1
        print("Se debe transformar cada label string en un label integer!")
        code_list = list(range(1,unique_labels_len+1))
        print(unique_labels)
        print(code_list)
        print("Creando el diccionario de labels ... ")
        dictionary_labels = dict(zip(unique_labels, code_list))
        print(dictionary_labels)
        y_train = y_train.map(dictionary_labels)
        y_test  = y_test.map(dictionary_labels)
        
        y_train_type = y_train.dtype
        y_test_type  = y_test.dtype
        print("y_train_type = " + str(y_train_type))
        print("y_test_type  = " + str(y_test_type))

    ##########################################################################################
    print("\nProcess vocabulary ...")
    print("max_vocab_length = " + str(max_vocab_length))
    vocab_processor = tf.contrib.learn.preprocessing.VocabularyProcessor(max_vocab_length)

    x_transform_train = vocab_processor.fit_transform(x_train)
    x_transform_test  = vocab_processor.transform(x_test)

    x_train_vocab = np.array(list(x_transform_train))
    x_test_vocab  = np.array(list(x_transform_test))

    vocab_len = len(vocab_processor.vocabulary_)
    print("Total words: vocab_len = " + str(vocab_len))

    ##########################################################################################
    print("\nBuild model ...")
    if model_mode == 0:
        model_case = rnn_model
    elif model_mode == 1:
        # Subtract 1 because:
        # VocabularyProcessor outputs a word-id matrix where word ids start from 1 and 0 means 'no word'. 
        # But categorical_column_with_identity assumes 0-based count and uses -1 for missing word.
        x_train_vocab -= 1
        x_test_vocab  -= 1
        model_case = bag_of_words_model

    model_parameters = {
                        'vocab_len': vocab_len,
                        'embedding_size': embedding_size,
                        'max_label': max_label
    }   
    classifier = tf.estimator.Estimator(model_fn = model_case, params = model_parameters)

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

    print("y_test      = ")
    print(y_test.as_matrix())
    print("y_predicted = ")
    print(y_predicted)
    if(dictionary_label_flag == 1):
        print(dictionary_labels)
    ##########################################################################################
    print("\nPerformance evaluation ...")

    score = metrics.accuracy_score(y_test, y_predicted)
    print("Accuracy (sklearn): score = " + str(round(score,4)))

    
    # TODOTODO: OBTENER f1
    # TODOTODO: OBTENER PRECITION
    # TODOTODO: OBTENRE RECALL
    # TODOTODO: OBTENER MATRIZ DE CONFUSIÓN (EN PLOTLY) (guardar HTML + PNG)

    print("DONE!")

if __name__ == "__main__":
        main()