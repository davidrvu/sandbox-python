# DAVIDRVU - 2017

from text_classifier import text_classifier
import argparse

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~        main all - TEXT CLASSIFICATION    ~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #############################################
    ## ARGUMENTS 
    #############################################
    print("ARGUMENTS AND PARAMETERS: ")
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
    
    text_classifier(debug, model_mode, file_in, fig_dir, train_perc, header_features, header_labels, max_vocab_length)

    print("DONE!")

if __name__ == "__main__":
        main()