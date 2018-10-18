# DAVIDRVU - 2018

# INSTALAR:
# pip install selenium
# pip install chromedriver
# pip install chromedriver-binary

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL_str = "http://www.yahoo.com"

#ex_path = "/usr/local/bin/chromedriver" # OJO REVISAR
ex_path = "C:/Anaconda3/Lib/site-packages/chromedriver"
browser = webdriver.Chrome(executable_path=ex_path)
browser.get(URL_str)



#assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

#browser.quit()