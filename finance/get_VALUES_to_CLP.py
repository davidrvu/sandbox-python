# DAVIDRVU 2018

from bs4 import BeautifulSoup
import datetime
import io
import requests
import sys
import urllib

def printdeb(debug, string_in):
    if debug == 1:
        print(string_in)

def url_req(url_in):
    try:
        resource = urllib.request.urlopen(url_in)
    except urllib.error.URLError:
        printdeb(debug, "\nERROR: No se puede conectar a la url = " + url_in)
        sys.exit()
    return resource

def resource_to_value(resource):
    content  = resource.read()
    charset  = resource.headers.get_content_charset()
    content  = content.decode(charset)
    
    soup = BeautifulSoup(content, 'html.parser')
    
    all_div = soup.html.body.findAll("div")
    
    data_span = str(all_div[-1].findAll("span"))
    current_value = float(data_span.split(">")[1].split("<")[0].split(" ")[0])

    return current_value

def get_VALUES_to_CLP(debug):
    url_USD_to_CLP = "https://finance.google.com/finance/converter?a=1&from=USD&to=CLP"
    url_EUR_to_CLP = "https://finance.google.com/finance/converter?a=1&from=EUR&to=CLP"
    printdeb(debug, "url_USD_to_CLP = " + url_USD_to_CLP)
    printdeb(debug, "url_EUR_to_CLP = " + url_EUR_to_CLP)
    
    current_time = datetime.datetime.now()

    resource_USD_to_CLP = url_req(url_USD_to_CLP)
    resource_EUR_to_CLP = url_req(url_EUR_to_CLP)

    current_USD_to_CLP = resource_to_value(resource_USD_to_CLP)
    current_EUR_to_CLP = resource_to_value(resource_EUR_to_CLP)

    printdeb(debug, str(current_time) + " 1 USD = " + str(current_USD_to_CLP) + " CLP   | 1 EURO = " + str(current_EUR_to_CLP))

    return [current_time, current_USD_to_CLP, current_EUR_to_CLP]

def main():
    print("get_USD_to_CLP testing ...")
    debug = 0
    [current_time, current_USD_to_CLP, current_EUR_to_CLP] = get_VALUES_to_CLP(debug)
    print(str(current_time) + " 1 USD = " + str(current_USD_to_CLP) + " CLP   | 1 EURO = " + str(current_EUR_to_CLP))
    print("DONE!")

if __name__ == "__main__":
    main() 