# -*- coding: utf-8 -*-

from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
#from urllib.request import urlopen
#from bs4 import BeautifulSoup


class Get_tables():

    def __init__(self):
        self.browser = webdriver.Chrome(r'D:\остальное\prog_DISK_C\chromedriver_win32\chromedriver.exe')

    def converter(self):
        data = pd.read_csv('D:\остальное\особо важное\всякая\BAD_inn100.csv', encoding='cp1251')
        inn = data['ИНН'].tolist()
        return inn

    def get_tbl(self, inn, iv=0):
        numerator = 0
        browser = self.browser
        for i in range(iv, 101):
            browser.get('https://www.audit-it.ru/buh_otchet/')
            xpath = browser.find_elements(By.CLASS_NAME, "buhotchet-search")

            inn_i = inn[i]
            y = str(inn_i)
            for link in xpath:
                try:
                    link.send_keys(str(y), Keys.ENTER)
                except:
                    print('errow')
            try:
                browser.find_element(By.XPATH, "/html/body/div[1]/section/section[2]/div[3]/div/table/tbody/tr[2]/td[2]/a").click()
                numerator += 1
            except:
                print('ИНН не найден')
                iv = i + 1
                return self.get_tbl(inn, iv)

            table_1 = len(browser.find_elements(By.CLASS_NAME, "tbl"))
            table_2 = len(browser.find_elements(By.CLASS_NAME, "tblFin"))
            for table1 in range(table_1):
                value1 = browser.find_elements(By.CLASS_NAME, "tbl")
                for val1 in value1:
                    with open('D:\остальное\особо важное\всякая\get_table3.csv', 'w', newline='') as csvfile:
                        wr = csv.writer(csvfile)
                        wr.writerow(str(numerator))
                        for row in val1.find_elements(By.CSS_SELECTOR, 'tr'):
                            wr.writerow([d.text for d in row.find_elements(By.CSS_SELECTOR, 'td')])
                    tabl1 = val1.text

                    print(tabl1)
'''
            for table2 in range(table_2):
                value2 = browser.find_elements(By.CLASS_NAME, "tblFin")
                for val2 in value2:
                    with open('D:\остальное\особо важное\всякая\get_table4.csv', 'w', newline='') as csvfile:
                        wr = csv.writer(csvfile)
                        wr.writerow(str(numerator))
                        for row in val2.find_elements(By.CSS_SELECTOR, 'tr'):
                            wr.writerow([d.text for d in row.find_elements(By.CSS_SELECTOR, 'td')])
                    tabl2 = val2.text
                    print(tabl2)'''
'''
            table_balance_1 = browser.find_element(By.CSS_SELECTOR, "#tblIdx1")
            table_koef = browser.find_elements(By.CLASS_NAME, "#tblFin")
            table_balance_2 = browser.find_element(By.CSS_SELECTOR, "#tblIdx2")
            with open('D:\остальное\особо важное\всякая\get_table3.csv', 'w', newline='') as csvfile:
                wr = csv.writer(csvfile)
                for row in table_balance_1.find_elements(By.CSS_SELECTOR, 'tr'):
                    wr.writerow([d.text for d in row.find_elements(By.CSS_SELECTOR, 'td')])
            df = pd.DataFrame(total)
            df.head(10)
            df.to_csv('G:\Books\html_tbl\get_table.csv', sep='\t', encoding='cp1251')

    def end(self):
        browser = self.browser
        browser.close()
'''

a = Get_tables()
b = a.converter()
a.get_tbl(b)
'a.end()'
