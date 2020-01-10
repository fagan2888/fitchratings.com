import time
import os
import shutil
from selenium import webdriver
from datetime import datetime
# datestring = datetime.strftime(datetime.now(), '(%Y-%m-%d)-(%H.%M.ss)')
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.request
import requests
import datetime

cwd = os.getcwd()
DRIVER = 'chromedriver'


chrome_options = webdriver.ChromeOptions()
if os.name == "nt":
  # If current OS is Windows
    chrome_options.add_argument("--start-maximized")
else:
    # Other OS (Mac / Linux)
    chrome_options.add_argument("--kiosk")


#------------------------------------------------------------------
driver = webdriver.Chrome(DRIVER, chrome_options = chrome_options)
driver.get('https://www.fitchratings.com/site/search?content=indonesia-issuercoverage')		
time.sleep(2)

all_html = driver.page_source
#soup = BeautifulSoup(all_html,"html.parser")
final_html = all_html 
soup = BeautifulSoup(final_html,"html.parser")
all_table = soup.find("div", attrs={"class":"entity-container table-responsive"})
#table =  soup.find("tr", attrs={"class":"entity-row showPointer"})
#print(all_table)
for x in range(12):
    for table in all_table.findAll('tr', attrs={"class":"entity-row showPointer"}):
        for list in table.findAll('td'):
            print(list.get_text(separator='\n'))
        # print(table.get_text())
        print("==========================")


    driver.find_element_by_link_text("Next").click()
    time.sleep(5)
    all_html = driver.page_source
    #soup = BeautifulSoup(all_html,"html.parser")
    final_html = all_html 
    soup = BeautifulSoup(final_html,"html.parser")
    all_table = soup.find("div", attrs={"class":"entity-container table-responsive"})

    # to_print = soup.findAll("tr", attrs={"class":"entity-row showPointer"})

    # print(to_print)