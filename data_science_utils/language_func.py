from langdetect import detect
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import re
import string
import sys

def language_func(full_text, lang_algorithm):  #Le entregas un string y te dice en qué idioma está
    puntuacion = set(string.punctuation) #Puntuacion
    full_text  = re.sub( '\s+', ' ', full_text).strip() # Reemplaza espacios multiples, por uno solo
    words      = ""
    if( full_text == "" or full_text == " "):
        detected_language = "NO_WORDS"
    else:
        #words = text.decode().encode('utf-8')
        words = full_text.lower()
        #words = ''.join(ch for ch in words if ch not in puntuacion) #Quito puntuacion y los reemplazo por espacios (PERO no deja un espacio)
        #words = ''.join([i for i in words if not i.isdigit()])      #Quito números y los reemplazo por espacios    (PERO no deja un espacio)
        #words = re.sub('[^a-zA-Z]+', ' ', words)   # Se reemplazan todos los caracteres que no sean letras por espacios (PERO también elimna ÁÉÍÓÚ)

        # Se reemplazan los caracteres de puntuación por espacios
        translator1 = re.compile('[%s]' % re.escape(string.punctuation))
        words = translator1.sub(' ', words)

        # Se reemplazan los caracteres de digitos por espacios
        translator2 = re.compile('[%s]' % re.escape(string.digits))
        words = translator2.sub(' ', words)

        words = re.sub( '\s+', ' ', words).strip() # Reemplaza espacios multiples, por uno solo
        if( words == "" or words == " "):
            detected_language = "NO_WORDS"
        else:
            if( lang_algorithm == 0): # PACKAGE: LANGDETECT
                try:
                    detected_language = detect(words)
                except:
                    print("\nERROR: NO se puede detectar el lenguaje en words = -" + words + "-\n")
                    sys.exit()

            elif( lang_algorithm == 1): # PACKAGE: WORD_TOKENIZE
                words = word_tokenize(words)  #Separo las palabras de cada línea
                languages_ratios = {}        
                for lang in stopwords.fileids():
                     stopwords_set = set(stopwords.words(lang))
                     words_set = set(words)
                     common_elements = words_set.intersection(stopwords_set)
                     languages_ratios[lang] = len(common_elements) # lang "score"
                detected_language = max(languages_ratios, key=languages_ratios.get)
            elif( lang_algorithm == 2): # PACKAGE: TextBlob   
                detected_language = TextBlob(words).detect_language()
            else:
                print("\nERROR: lang_algorithm = " + str(lang_algorithm) +" NO VALIDO. \n")
                sys.exit()

    return [detected_language, words]