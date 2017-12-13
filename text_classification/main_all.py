# DAVIDRVU - 2017

from sklearn import metrics
import argparse
import numpy as np
import pandas as pd
import sys
import tensorflow as tf

sys.path.insert(0, '..//data_science_utils')
from classification_algorithm_performance import classification_algorithm_performance
from get_dir_file_ext import get_dir_file_ext
from pandas_read_csv import pandas_read_csv
from pandas_write_csv import pandas_write_csv
from split_datasets import split_datasets

def estimator_spec_for_softmax_classification(logits, labels, mode, params): # model_mode == 0 & 1
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


def bag_of_words_model(features, labels, mode, params): #model_mode == 0: # bag_of_words_model
    """A bag-of-words model. Note it disregards the word order in the text."""
    bow_column           = tf.feature_column.categorical_column_with_identity(params['feature_name'], num_buckets=params['vocab_len'])
    bow_embedding_column = tf.feature_column.embedding_column(bow_column, dimension=params['embedding_size'])   
    bow                  = tf.feature_column.input_layer(features, feature_columns=[bow_embedding_column])
    logits               = tf.layers.dense(bow, params['max_label'], activation=None)

    return estimator_spec_for_softmax_classification(logits=logits, labels=labels, mode=mode, params=params)


def rnn_model(features, labels, mode, params): # model_mode == 1: # rnn_model    
    """RNN model to predict from sequence of words to a class."""
    # Convert indexes of words into embeddings. This creates embeddings matrix of [vocab_len, embedding_size] and then maps word indexes of the sequence into [batch_size, sequence_length, embedding_size].
    word_vectors = tf.contrib.layers.embed_sequence(features[params['feature_name']], vocab_size=params['vocab_len'], embed_dim=params['embedding_size'])

    # Split into list of embedding per word, while removing doc length dim. word_list results to be a list of tensors [batch_size, embedding_size].
    word_list = tf.unstack(word_vectors, axis=1)

    # Create a Gated Recurrent Unit cell with hidden size of embedding_size.
    cell = tf.nn.rnn_cell.GRUCell(params['embedding_size'])

    # Create an unrolled Recurrent Neural Networks to length of max_vocab_length and passes word_list as inputs for each unit.
    _, encoding = tf.nn.static_rnn(cell, word_list, dtype=tf.float32)

    # Given encoding of RNN, take encoding of last step (e.g hidden size of the neural network of last step) and pass it as features for softmax classification over output classes.
    logits = tf.layers.dense(encoding, params['max_label'], activation=None)

    return estimator_spec_for_softmax_classification(logits=logits, labels=labels, mode=mode, params=params)


def cnn_model(features, labels, mode, params): # model_mode == 2: # Cnn_model  
    """2 layer ConvNet to predict from sequence of words to a class."""
    # Convert indexes of words into embeddings.This creates embeddings matrix of [params['vocab_len'], EMBEDDING_SIZE] and then maps word indexes of the sequence into [batch_size, sequence_length, EMBEDDING_SIZE].
    word_vectors = tf.contrib.layers.embed_sequence(features[params['feature_name']], vocab_size=params['vocab_len'], embed_dim=params['embedding_size'])
    word_vectors = tf.expand_dims(word_vectors, 3)
    with tf.variable_scope('CNN_Layer1'): # Apply Convolution filtering on input sequence.
        conv1 = tf.layers.conv2d(word_vectors, filters=params['n_filters'], kernel_size=params['filter_shape1'], padding='VALID', activation=tf.nn.relu) # Add a ReLU for non linearity.
        # Max pooling across output of Convolution+Relu.
        pool1 = tf.layers.max_pooling2d(conv1, pool_size=params['pooling_window'], strides=params['pooling_stride'], padding='SAME')
        # Transpose matrix so that params['n_filters'] from convolution becomes width.
        pool1 = tf.transpose(pool1, [0, 1, 3, 2])

    with tf.variable_scope('CNN_Layer2'): # Second level of convolution filtering.
        conv2 = tf.layers.conv2d(pool1, filters=params['n_filters'], kernel_size=params['filter_shape2'], padding='VALID')
        # Max across each filter to get useful features for classification.
        pool2 = tf.squeeze(tf.reduce_max(conv2, 1), squeeze_dims=[1])

    # Apply regular WX + B and classification.
    logits = tf.layers.dense(pool2, params['max_label'], activation=None)

    predicted_classes = tf.argmax(logits, 1)
    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions={'class': predicted_classes, 'prob': tf.nn.softmax(logits)})

    onehot_labels = tf.one_hot(labels, params['max_label'], 1, 0)
    loss = tf.losses.softmax_cross_entropy(onehot_labels=onehot_labels, logits=logits)
    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
        train_op  = optimizer.minimize(loss, global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode, loss=loss, train_op=train_op)

    eval_metric_ops = {'accuracy': tf.metrics.accuracy(labels=labels, predictions=predicted_classes)}
    return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)


def char_rnn_model(features, labels, mode, params): # model_mode == 3: # character rnn model
    """Character level recurrent neural network model to predict classes."""
    byte_vectors = tf.one_hot(features[params['feature_name']], 256, 1., 0.)
    byte_list    = tf.unstack(byte_vectors, axis=1)

    cell = tf.nn.rnn_cell.GRUCell(params['hidden_size'])
    _, encoding = tf.nn.static_rnn(cell, byte_list, dtype=tf.float32)

    logits = tf.layers.dense(encoding, params['max_label'], activation=None)

    predicted_classes = tf.argmax(logits, 1)
    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions={'class': predicted_classes, 'prob': tf.nn.softmax(logits)})

    onehot_labels = tf.one_hot(labels, params['max_label'], 1, 0)
    loss = tf.losses.softmax_cross_entropy(onehot_labels=onehot_labels, logits=logits)
    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
        train_op  = optimizer.minimize(loss, global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode, loss=loss, train_op=train_op)

    eval_metric_ops = {'accuracy': tf.metrics.accuracy(labels=labels, predictions=predicted_classes)}
    return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)


def char_cnn_model(features, labels, mode, params): # model_mode == 4: # character cnn model
    """Character level convolutional neural network model to predict classes."""
    features_onehot = tf.one_hot(features[params['feature_name']], 256)
    input_layer     = tf.reshape(features_onehot, [-1, params['max_document_length'], 256, 1])

    with tf.variable_scope('CNN_Layer1'):
        # Apply Convolution filtering on input sequence.
        conv1 = tf.layers.conv2d(input_layer, filters=params['n_filters'], kernel_size=params['filter_shape1'], padding='VALID', activation=tf.nn.relu) # Add a ReLU for non linearity.
        # Max pooling across output of Convolution+Relu.
        pool1 = tf.layers.max_pooling2d(conv1, pool_size=params['pooling_window'], strides=params['pooling_stride'], padding='SAME')
        # Transpose matrix so that n_filters from convolution becomes width.
        pool1 = tf.transpose(pool1, [0, 1, 3, 2])

    with tf.variable_scope('CNN_Layer2'):
        # Second level of convolution filtering.
        conv2 = tf.layers.conv2d(pool1, filters=params['n_filters'], kernel_size=params['filter_shape2'], padding='VALID')
        # Max across each filter to get useful features for classification.
        pool2 = tf.squeeze(tf.reduce_max(conv2, 1), squeeze_dims=[1])

    # Apply regular WX + B and classification.
    logits = tf.layers.dense(pool2, params['max_label'], activation=None)

    predicted_classes = tf.argmax(logits, 1)

    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions={'class': predicted_classes, 'prob': tf.nn.softmax(logits)})

    onehot_labels = tf.one_hot(labels, params['max_label'], 1, 0)
    loss = tf.losses.softmax_cross_entropy(onehot_labels=onehot_labels, logits=logits)

    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
        train_op = optimizer.minimize(loss, global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode, loss=loss, train_op=train_op)

    eval_metric_ops = {'accuracy': tf.metrics.accuracy(labels=labels, predictions=predicted_classes)}
    return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)


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
    parser.add_argument('--model_mode',       type=int,             default=0,    help='a model_mode flag')
    parser.add_argument('--file_in',          type=str, nargs='+',  default=[],   help='input file')
    parser.add_argument('--train_perc',       type=float,           default=0.89, help='train set percentage')
    parser.add_argument('--header_features',  type=str, nargs='+',  default=[],   help='header features (raw text)')
    parser.add_argument('--header_labels',    type=str, nargs='+',  default=[],   help='header labels')
    parser.add_argument('--max_vocab_length', type=int,             default=15,   help='max vocabulary length')
    parser.add_argument('--fig_dir',          type=str, nargs='+',  default=[],   help='Directory for figures')

    args = parser.parse_args()

    debug            = args.debug
    model_mode       = args.model_mode
    file_in          = args.file_in[0]
    train_perc       = args.train_perc
    header_features  = args.header_features[0]
    header_labels    = args.header_labels[0]
    max_vocab_length = args.max_vocab_length
    fig_dir          = args.fig_dir[0]

    print("_________________________________________________________")
    print("_________________ARGUMENTS_______________________________")
    print("debug            = " + str(debug))
    print("model_mode       = " + str(model_mode))
    print("file_in          = " + file_in)
    print("fig_dir          = " + fig_dir)
    print("train_perc       = " + str(train_perc))
    print("header_features  = " + header_features)
    print("header_labels    = " + header_labels)
    print("max_vocab_length = " + str(max_vocab_length))
    print("_________________________________________________________")
    
    ##########################################################################################
    print("\nLoad FULL dataset and split it ... ")
    
    split_datasets(file_in, train_perc, header_labels, final_sort = True)
    [directory, filename_in_base, ext] = get_dir_file_ext(file_in)
    file_train   = directory + "//" + filename_in_base + "_train.csv"
    file_test    = directory + "//" + filename_in_base + "_test.csv"
    file_predict = directory + "//" + filename_in_base + "_output_predict.csv"

    ##########################################################################################
    print("\nRead train and test datasets ... ")
    df_train = pandas_read_csv(file_train) 
    df_test  = pandas_read_csv(file_test) 

    x_train  = pd.Series(df_train[header_features]) # FEATURES
    y_train  = pd.Series(df_train[header_labels])   # LABELS

    x_test   = pd.Series(df_test[header_features])  # FEATURES
    y_test   = pd.Series(df_test[header_labels])    # LABELS

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
    x_train_type = x_train.dtype
    x_test_type  = x_test.dtype
    y_train_type = y_train.dtype
    y_test_type  = y_test.dtype
    print("x_train_type = " + str(x_train_type))
    print("x_test_type  = " + str(x_test_type))
    print("y_train_type = " + str(y_train_type))
    print("y_test_type  = " + str(y_test_type))

    if (y_train_type == "object" or y_test_type == "object"):
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
    else:
        dictionary_labels = None

    ##########################################################################################

    if model_mode == 0: # bag_of_words_model
        print("\n=============> model_mode = 1: bag_of_words_model")
        print("\nSetting model parameters ...")
        embedding_size  = 50

        print("\nProcess vocabulary ...")
        print("max_vocab_length = " + str(max_vocab_length))
        vocab_processor = tf.contrib.learn.preprocessing.VocabularyProcessor(max_vocab_length)
        x_train_vocab   = np.array(list(vocab_processor.fit_transform(x_train)))
        x_test_vocab    = np.array(list(vocab_processor.transform(x_test)))

        vocab_len = len(vocab_processor.vocabulary_)
        print("Total words: vocab_len = " + str(vocab_len))

        print("\nBuild model ...")
        # Subtract 1 because:
        # VocabularyProcessor outputs a word-id matrix where word ids start from 1 and 0 means 'no word'. 
        # But categorical_column_with_identity assumes 0-based count and uses -1 for missing word.
        x_train_vocab -= 1
        x_test_vocab  -= 1
        feature_name = 'words'
        model_parameters = {'feature_name': feature_name, 'vocab_len': vocab_len, 'embedding_size': embedding_size, 'max_label': max_label}
        batch_size_param = len(x_train_vocab)
        model_case = bag_of_words_model

    elif model_mode == 1: # rnn_model
        print("\n=============> model_mode = 0: rnn_model")
        print("\nSetting model parameters ...")
        embedding_size  = 50

        print("\nProcess vocabulary ...")
        print("max_vocab_length = " + str(max_vocab_length))
        vocab_processor = tf.contrib.learn.preprocessing.VocabularyProcessor(max_vocab_length)
        x_train_vocab   = np.array(list(vocab_processor.fit_transform(x_train)))
        x_test_vocab    = np.array(list(vocab_processor.transform(x_test)))

        vocab_len = len(vocab_processor.vocabulary_)
        print("Total words: vocab_len = " + str(vocab_len))

        print("\nBuild model ...")
        feature_name = 'words'
        model_parameters = {'feature_name': feature_name, 'vocab_len': vocab_len, 'embedding_size': embedding_size, 'max_label': max_label}
        batch_size_param = len(x_train_vocab)
        model_case = rnn_model

    elif model_mode == 2: # cnn_model
        print("\n=============> model_mode = 4: cnn_model")
        print("\nSetting model parameters ...")
        max_document_length = 100
        embedding_size      = 20
        n_filters           = 10
        window_size         = 20
        filter_shape1       = [window_size, embedding_size]
        filter_shape2       = [window_size, n_filters]
        pooling_window      = 4
        pooling_stride      = 2

        print("\nProcess vocabulary ...")
        vocab_processor = tf.contrib.learn.preprocessing.VocabularyProcessor(max_document_length)
        x_train_vocab   = np.array(list(vocab_processor.fit_transform(x_train)))
        x_test_vocab    = np.array(list(vocab_processor.transform(x_test)))

        vocab_len = len(vocab_processor.vocabulary_)
        print("Total words: vocab_len = " + str(vocab_len))

        print("\nBuild model ...")
        feature_name = 'words'
        model_parameters = {'feature_name': feature_name, 'vocab_len': vocab_len, 'max_document_length': max_document_length, 'embedding_size': embedding_size, 'n_filters': n_filters, 'window_size': window_size, 'filter_shape1': filter_shape1, 'filter_shape2': filter_shape2, 'pooling_window': pooling_window, 'pooling_stride': pooling_stride, 'max_label': max_label}
        batch_size_param = len(x_train_vocab)
        model_case = cnn_model

    elif model_mode == 3: # character rnn model
        print("\n=============> model_mode = 3: character rnn")
        print("\nSetting model parameters ...")
        max_document_length = 100
        hidden_size         = 20

        print("\nProcess vocabulary ...")
        char_processor = tf.contrib.learn.preprocessing.ByteProcessor(max_document_length)
        x_train_vocab  = np.array(list(char_processor.fit_transform(x_train)))
        x_test_vocab   = np.array(list(char_processor.transform(x_test)))

        print("\nBuild model ...")
        feature_name = 'chars'
        model_parameters = {'feature_name': feature_name, 'max_document_length': max_document_length, 'hidden_size': hidden_size, 'max_label': max_label}
        batch_size_param = 128
        model_case = char_rnn_model

    elif model_mode == 4: # character cnn model
        print("\n=============> model_mode = 2: character cnn")
        print("\nSetting model parameters ...")
        max_document_length = 100
        n_filters           = 10 
        filter_shape1       = [20, 256]
        filter_shape2       = [20, n_filters]
        pooling_window      = 4
        pooling_stride      = 2

        print("\nProcess vocabulary ...")
        char_processor = tf.contrib.learn.preprocessing.ByteProcessor(max_document_length)
        x_train_vocab  = np.array(list(char_processor.fit_transform(x_train)))
        x_test_vocab   = np.array(list(char_processor.transform(x_test)))
        x_train_vocab  = x_train_vocab.reshape([-1, max_document_length, 1, 1])
        x_test_vocab   = x_test_vocab.reshape([-1, max_document_length, 1, 1])

        print("\nBuild model ...")
        feature_name = 'chars'
        model_parameters = {'feature_name': feature_name, 'max_document_length': max_document_length, 'n_filters': n_filters, 'filter_shape1': filter_shape1, 'filter_shape2': filter_shape2, 'pooling_window': pooling_window, 'pooling_stride': pooling_stride, 'max_label': max_label}
        batch_size_param = 128
        model_case = char_cnn_model

    else:
        print("\nERROR: model_mode = " + str(model_mode) + " NO EXISTE.")
        sys.exit()

    print("\nClassifier ...")  
    classifier = tf.estimator.Estimator(model_fn = model_case, params = model_parameters)

    print("\nTraining ...")
    train_input_fn = tf.estimator.inputs.numpy_input_fn(x={model_parameters['feature_name']: x_train_vocab}, y=y_train, batch_size=batch_size_param, num_epochs=None, shuffle=True)
    classifier.train(input_fn=train_input_fn, steps=100)

    print("\nPredict ...")
    test_input_fn = tf.estimator.inputs.numpy_input_fn(x={model_parameters['feature_name']: x_test_vocab}, y=y_test, num_epochs=1, shuffle=False)

    predictions = classifier.predict(input_fn=test_input_fn)
    y_predicted = np.array(list(p["class"] for p in predictions))
    y_predicted = y_predicted.reshape(np.array(y_test).shape)

    print("y_test      = ")
    print(y_test.as_matrix())
    print("y_predicted = ")
    print(y_predicted)
    print("dictionary_labels = ")
    print(dictionary_labels)

    figure_name = fig_dir + "confusion_" + filename_in_base + "_model_mode_" + str(model_mode) 
    classification_algorithm_performance(y_test, y_predicted, figure_name, dictionary_labels, unique_labels)

    #############################################
    ## Se guarda archivo con resultados de predicción y sus características respectivas
    #############################################
    y_test_str      = [None] * y_test.size
    y_predicted_str = [None] * y_test.size
    if dictionary_labels is None:
        print("No hay diccionario!")
        for i in range(0, y_test.size):
            y_test_str[i]      = str(y_test[i])
            y_predicted_str[i] = str(y_predicted[i])           
    else: 
        print("Hay diccionario!")
        inv_dictionary_labels = {v: k for k, v in dictionary_labels.items()}
        for i in range(0, y_test.size):
            y_test_str[i]      = inv_dictionary_labels.get(y_test[i])
            y_predicted_str[i] = inv_dictionary_labels.get(y_predicted[i])

    y_check = [None] * y_test.size
    for i in range(0, y_test.size):        
        if y_predicted[i] == y_test[i]:
            y_check[i] = "True"
        else:
            y_check[i] = "False"
    df_x_test      = pd.DataFrame(data=x_test.values,   columns=['x_test'])
    df_y_test      = pd.DataFrame(data=y_test_str,      columns=['y_test'])
    df_y_predicted = pd.DataFrame(data=y_predicted_str, columns=['y_predicted'])
    df_y_check     = pd.DataFrame(data=y_check,         columns=['y_check'])
    df_output      = pd.concat([df_x_test, df_y_test, df_y_predicted, df_y_check], axis=1)
    pandas_write_csv(df_output, file_predict)

    print("DONE!")

if __name__ == "__main__":
        main()