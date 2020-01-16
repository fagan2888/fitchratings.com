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



wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1') 

sheet1.write(0, 0, 'ENTITIY') 
sheet1.write(0, 1, 'RATING') 
sheet1.write(0, 3, '') 
sheet1.write(0, 4, '') 
sheet1.write(0, 5, '') 
sheet1.write(0, 6, 'SECTOR') 
sheet1.write(0, 7, 'COUNTRY') 
sheet1.write(0, 8, 'ANALYSTS') 



chrome_options = webdriver.ChromeOptions()
if os.name == "nt":
  
    chrome_options.add_argument("--start-maximized")
else:
    
    chrome_options.add_argument("--kiosk")


driver = webdriver.Chrome(DRIVER, chrome_options = chrome_options)
driver.get('https://www.fitchratings.com/site/search?content=indonesia-issuercoverage')		
time.sleep(5)

all_html = driver.page_source

final_html = all_html 
soup = BeautifulSoup(final_html,"html.parser")
all_table = soup.find("div", attrs={"class":"entity-container table-responsive"})


substring_idn = "idn"
row = 1 
col = 0
for x in range(13):
    print("page ",x+1)
    
    for table in all_table.findAll('tr', attrs={"class":"entity-row showPointer"}):
        nomor = 1

        symbol_one = ""
        symbol_two = ""
        for list in table.findAll('tr', attrs={"class":"rating"}):
            for stable in list.findAll('span'):
                classNama = ''.join(stable['class'])
                seperateClassName=classNama.replace("alert-descriptionratings-","")
                if seperateClassName != "":                  
                    symbol_one = seperateClassName
                    spliter = symbol_one.split('-')
                    print (len(spliter))
                    print(spliter[0].capitalize(), spliter[1].capitalize())
                elif  seperateClassName == "":
                    
                    symbol_two = "-"

        for list in table.findAll('td'):

            if nomor == 1:
                item = list.get_text().replace("Ultimate Parent","").replace("LATEST RATING ACTION COMMENTARY","").replace("VIEW RESEARCH","")
            else:
                item = list.get_text(separator=' ')
            
            combine = str(nomor)+item
            
            bolean_nya = combine.count(substring_idn)
            if nomor == 2:
                item = spliter[0].capitalize()
                if symbol_one == "":
                    item = "-"

                
            if nomor == 3:
                col = col + 1
            if nomor == 7 and bolean_nya == 0 :
                nomor = 11
            if nomor == 7 and bolean_nya == 1:
                item = item 
                row = row+1
                col = 3
                sheet1.write(row, col-1, symbol_two)
                sheet1.write(row, col-2, symbol_two)

            combine = str(nomor)+" "+ item
            print(combine)
            sheet1.write(row, col, item)
            if nomor == 2:
                if symbol_one == "":
                    item = "-"
                    spliter[1]="-"
                sheet1.write(row, col+1, spliter[1].capitalize())
            wb.save('fitchratings.xls')
            nomor = nomor + 1
            col = col+1
            
            

            
            
            
        

        row = row+1
        print("==========================")
        col = 0
     
    driver.find_element_by_link_text("Next").click()
    time.sleep(5)
    all_html = driver.page_source
    
    final_html = all_html 
    soup = BeautifulSoup(final_html,"html.parser")
    all_table = soup.find("div", attrs={"class":"entity-container table-responsive"})
    

    

    


