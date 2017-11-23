from langdetect import detect
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import string

def language(full_text):  #Le entregas un string y te dice en qué idioma está
    detect_algorithm = 2

    puntuacion = set(string.punctuation) #Puntuacion
    #words = text.decode().encode('utf-8')
    words = full_text.lower()
    words = ''.join(ch for ch in words if ch not in puntuacion) #Quito puntuacion
    words = ''.join([i for i in words if not i.isdigit()])      #Quito números

    if( detect_algorithm == 0):
        detected_language = detect(words)

    elif( detect_algorithm == 1):
        words = word_tokenize(words)                                #Separo las palabras de cada línea
        languages_ratios = {}        
        for language in stopwords.fileids():
             stopwords_set = set(stopwords.words(language))
             words_set = set(words)
             common_elements = words_set.intersection(stopwords_set)
             languages_ratios[language] = len(common_elements) # language "score"
        most_rated_language = max(languages_ratios, key=languages_ratios.get)

    elif( detect_algorithm == 2): # PACKAGE: TextBlob   
        detected_language = TextBlob(words).detect_language()
        print(detected_language)
    else:
        print("\nERROR: detect_algorithm = " + str(detect_algorithm) +" NO VALIDO. \n")
        sys.exit()

    return detected_language

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~ LANGUAGE DETECTOR ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    text1 = "¿hola como estás?"
    text2 = "where are you from?"
    text3 = "Estou bem, obrigado"
    text4 = "Programar es lo mejor"
    text5 = "May the force be with you!"
    text6 = "Dziękuję"

    print("text1 = " + text1)
    print("text2 = " + text2)
    print("text3 = " + text3)
    print("text4 = " + text4)
    print("text5 = " + text5)
    print("text6 = " + text6)   

    print("\n")

    detect1 = language(text1)
    detect2 = language(text2)
    detect3 = language(text3)
    detect4 = language(text4)
    detect5 = language(text5)
    detect6 = language(text6)

    print("detect1 = " + detect1)
    print("detect2 = " + detect2) 
    print("detect3 = " + detect3) 
    print("detect4 = " + detect4) 
    print("detect5 = " + detect5) 
    print("detect6 = " + detect6) 

if __name__ == "__main__":
    main()