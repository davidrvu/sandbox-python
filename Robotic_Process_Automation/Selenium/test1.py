# DAVIDRVU - 2018

# 1) INSTALAR:
#      pip install selenium
# 2) DESCARGAR CHROMEDRIVER DE:
#      https://sites.google.com/a/chromium.org/chromedriver/downloads
#      VERSION: chromedriver_win32.zip
# 3) Poner en PATH el archivo chromedriver.exe
# 4) EJECUTAR ESTE SCRIPT!

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():
    print("==============================================")
    print("     selenium Test 1                          ")
    print("==============================================")

    start_time = time.time()

    URL_str = "http://www.yahoo.com"
    browser = webdriver.Chrome()
    browser.get(URL_str)

    elem = browser.find_element_by_name('p')  # Find the search box
    elem.send_keys('seleniumhq' + Keys.RETURN)


 
    end_time   = time.time()
    total_time_seconds = end_time - start_time
    total_time = time.strftime("%H:%M:%S", time.gmtime(total_time_seconds))
    print("total_time = " + str(total_time))


    #browser.quit()
    print("DONE!")


if __name__ == "__main__":
    main()