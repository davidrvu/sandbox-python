# DAVIDRVU - 2017
# Crea base de datos fake para clasificar texto en base a palabras repetidas

from nltk.corpus import stopwords
from random import randint
import pandas as pd
import sys

sys.path.insert(0, '..//data_science_utils')
from pandas_write_csv import pandas_write_csv

def main():

    ###################################################
    ## SET PARAMETERS
    ###################################################
    samples_per_class = [9000, 1000, 500] 
    labels            = ["canino", "felino", "reptil"]
    key_words         = ["perro", "gato", "lagarto"]
    min_text_size     = 20
    max_text_size     = 40
    num_classes       = len(labels)
    num_samples       = sum(samples_per_class)
    output_filename   = "C:\\davidrvu\\data_bases\\fake_data\\fake_" + str(num_classes)+ "clases_" + str(num_samples) + "samples.csv"
    
    ###################################################
    ## SHOW PARAMETERS
    ###################################################
    print("num_samples     = " + str(num_samples))
    print("num_classes     = " + str(num_classes))
    print("output_filename = " + output_filename)

    ###################################################
    ## Create new data
    ###################################################
    conectores_esp     = stopwords.words("spanish")
    conectores_eng     = stopwords.words("english")
    conectores_por     = stopwords.words("portuguese")
    conectores_ALL     = conectores_esp + conectores_eng + conectores_por
    conectores_ALL_len = len(conectores_ALL)

    text_all   = [None] * num_samples
    labels_all = [None] * num_samples
    current_row = 0
    for clase in range(0, num_classes):
        for muestra in range(0, samples_per_class[clase]):
            num_words = randint(min_text_size, max_text_size)
            current_words = 0
            current_text  = ""
            while (current_words <= num_words):
                if(current_words%2 == 0): # Si es par
                    current_text = current_text + key_words[clase]
                else: # Si es impar
                    current_conector = conectores_ALL[randint(0, conectores_ALL_len-1)]
                    current_text     = current_text + " " + current_conector + " "
                current_words = current_words + 1
            text_all[current_row]   = current_text
            labels_all[current_row] = labels[clase]
            current_row = current_row + 1

    outputDataFrame = pd.DataFrame(data={"content":text_all, "class":labels_all})
    print(outputDataFrame)
    pandas_write_csv(outputDataFrame, output_filename)

if __name__ == "__main__":
        main()