#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#import library of database
import pandas as pd
#import Manage_db
from Get_Data_Country.DataBase import write_data

DB = write_data()


ser = Service('C:\Program Files\JetBrains\PyCharm 2019.2.4\chromedriver.exe')
str_country = '//*[@id="mw-pages"]/div/div/div[1]/ul/li[1]/a'
str_company = '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[1]/td[1]'
xpath = []


class WikiCountry:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ser)

    def open_page(self):
        driver = self.driver
        driver.get('https://en.wikipedia.org/wiki/Category:Lists_of_companies_by_country')
        return driver

    def get_list_country(self, driver, NUMERATOR_i):
        try:
            for i in range(NUMERATOR_i, 26):
                NUMERATOR_i += 1
                for j in range(1, 26):
                    print(i)
                    print(j)
                    name_company = 0
                    name_industry = 0
                    name_sector = 0
                    list_country = list(str_country)
                    list_country[32] = str(i)
                    list_country[41] = str(j)
                    list_country_join = ''.join(list_country)
                    xpath_country = driver.find_element(by=By.XPATH, value=list_country_join)
                    name_country = xpath_country.text
                    name_country_str = str(name_country)
                    name_country = name_country_str.replace("List of companies of ", "")
                    print(name_country)
                    xpath_country.click()
                    try:
                        for n in range(1, 10000):
                            Data_company = []
                            for m in range(1, 4):
                                print(n)
                                print(m)
                                list_company = list(str_company)
                                list_company[49] = str(n)
                                list_company[55] = str(m)
                                list_company_join = ''.join(list_company)
                                xpath_company = driver.find_element(by=By.XPATH, value=list_company_join)
                                Data_company.append(xpath_company.text)
                                if m == 1:
                                    name_company = Data_company[0]
                                    print(name_company)
                                elif m == 2:
                                    name_industry = Data_company[1]
                                    print(name_industry)
                                elif m == 3:
                                    name_sector = Data_company[2]
                                    print(name_sector)
                            DB.insert_table(n, name_country, name_company, name_industry, name_sector)
                    except Exception as exc_company:
                        print('errow_Company: ' + str(exc_company))
                        driver.get('https://en.wikipedia.org/wiki/Category:Lists_of_companies_by_country')
        except Exception as exc_county:
            print('ERROW_Country: ' + str(exc_county))
            self.get_list_country(driver, NUMERATOR_i)

obj = WikiCountry()
a = obj.open_page()
obj.get_list_country(a, 1)
