# DAVIDRVU - 2018

from language_func import language_func
from nltk.corpus import stopwords
import os
import sys
import time

def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]

def preprocessingRawTextGetLang(input_text):
    #################################################################
    ## preprocessing0 (elimina algunos caracteres que no son de utilidad.)
    #################################################################

    input_text = input_text.replace(',', ' ')
    input_text = input_text.replace(';', ' ')
    input_text = input_text.replace('/', ' ')
    input_text = input_text.replace('\n', ' ')
    input_text = input_text.replace('\r', ' ')
    input_text = input_text.replace('\t', ' ')
    input_text = input_text.replace('\nr', ' ')
    input_text = input_text.replace('<br>', ' ')

    if ((input_text == " ") or (input_text == "")):
        return [None, None, None]

    #################################################################
    ## preprocessing1 (# Se agrega idioma, se deja sin puntuación, sin digitos, y sin espacios consecutivos)
    #################################################################
    lang_algorithm = 0 # LANGDETECT

    [language_detected, words_filtered] = language_func(input_text, lang_algorithm)

    if ((words_filtered == " ") or (words_filtered == "EMPTY") or (words_filtered == "empty")):
        return [None, None, None]

    if ((language_detected == " ") or (language_detected == "NO_WORDS")):
        return [None, None, None]

    #################################################################
    ## preprocessing2 (Se eliminan los conectores en español, portugues e inglés)
    #################################################################
    conectores_esp     = stopwords.words("spanish")
    conectores_eng     = stopwords.words("english")
    conectores_por     = stopwords.words("portuguese")
    conectores_ALL     = conectores_esp + conectores_eng + conectores_por

    try:
        conectores_ALL = remove_values_from_list(conectores_ALL, "la")
        conectores_ALL = remove_values_from_list(conectores_ALL, "m")
        conectores_ALL = remove_values_from_list(conectores_ALL, "os")
        conectores_ALL = remove_values_from_list(conectores_ALL, "a")
        conectores_ALL = remove_values_from_list(conectores_ALL, "o")
        conectores_ALL = remove_values_from_list(conectores_ALL, "e")
        conectores_ALL = remove_values_from_list(conectores_ALL, "ao")
        conectores_ALL = remove_values_from_list(conectores_ALL, "eu")
    except ValueError:
        pass

    words_filtered_sin_conect = ' '.join([word for word in words_filtered.split() if word not in (conectores_ALL)])

    return [words_filtered, words_filtered_sin_conect, language_detected]


def main():
    print("-> Start preprocessingRawTextGetLang ")

    test1_in  = "!%&# Test1, ? desde hasta 345Code: para 34HH"
    #test1_in  = "!%&234"
    #test1_in  = "desde hasta para 12345" # SOLO CONECTORES

    start_time = time.time()
    [test1_out, test1_out_sin_conect, test1_lang] = preprocessingRawTextGetLang(test1_in)
    end_time   = time.time()
    
    print("test1_in              = " + str(test1_in))
    print("test1_out             = " + str(test1_out))
    print("test1_out_sin_conect  = " + str(test1_out_sin_conect))
    print("test1_lang            = " + str(test1_lang))
    print("Tiempo : " + str(end_time - start_time) + " segundos")
    print("\nDone!")

if __name__ == "__main__":
    main()