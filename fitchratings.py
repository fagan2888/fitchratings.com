import time
import os
import shutil
from selenium import webdriver
from datetime import datetime
from bs4 import BeautifulSoup
import urllib.request
import requests
import datetime
import xlwt 
from xlwt import Workbook

cwd = os.getcwd()
DRIVER = 'chromedriver'

#===============================

# outfile_name = "TableFithcRatings.csv"
# headers = "ENTITIY,RATING, , , ,SECTOR,COUNTRY,ANALYSTS \n"
# f = open(outfile_name, "w")
# f.write(headers)
# f.close()
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1') 

sheet1.write(0, 0, 'ENTITIY') 
sheet1.write(0, 2, 'RATING') 
sheet1.write(0, 3, '') 
sheet1.write(0, 4, '') 
sheet1.write(0, 5, '') 
sheet1.write(0, 6, 'SECTOR') 
sheet1.write(0, 7, 'COUNTRY') 
sheet1.write(0, 8, 'ANALYSTS') 



#=================================

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
time.sleep(5)

all_html = driver.page_source
#soup = BeautifulSoup(all_html,"html.parser")
final_html = all_html 
soup = BeautifulSoup(final_html,"html.parser")
all_table = soup.find("div", attrs={"class":"entity-container table-responsive"})
#table =  soup.find("tr", attrs={"class":"entity-row showPointer"})
#print(all_table)
substring_idn = "idn"
row = 1 
col = 0
for x in range(13):
    print("page ",x+1)
    
    for table in all_table.findAll('tr', attrs={"class":"entity-row showPointer"}):
        nomor = 1
        list = []
        # a[nomor] = ""
        for list in table.findAll('td'):
           
            # item = list.get_text(separator='\n').split('\n')
            #list
            if nomor == 1:
                item = list.get_text(separator=' | ')
            else:
                item = list.get_text(separator=' ')
            #combine = item+str(nomor)
            combine = str(nomor)+item
            
            bolean_nya = combine.count(substring_idn)
            if nomor == 2:
                item = ""
            if nomor == 7 and bolean_nya == 0 :
                nomor = 11
            if nomor == 7 and bolean_nya == 1:
                row = row+1
                col = 2
            combine = str(nomor)+item
            print(combine)
            sheet1.write(row, col, item) 
            wb.save('fitchratings.xls')
            nomor = nomor + 1
            col = col+1
            
            # if nomor == 7 0:

            
            # if nomor = 2:
            #     print(list.get_text(seperator='\n') 
        # print(table.get_text())
        row = row+1
        print("==========================")
        col = 0
     
    driver.find_element_by_link_text("Next").click()
    time.sleep(5)
    all_html = driver.page_source
    #soup = BeautifulSoup(all_html,"html.parser")
    final_html = all_html 
    soup = BeautifulSoup(final_html,"html.parser")
    all_table = soup.find("div", attrs={"class":"entity-container table-responsive"})
    

    # to_print = soup.findAll("tr", attrs={"class":"entity-row showPointer"})

    # print(to_print)