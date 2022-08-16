# -*- coding: utf-8 -*-

from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

class GetInfoData:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ser)

    def open_page(self):
        driver = self.driver
        driver.get('https://en.wikipedia.org/wiki/Category:Lists_of_companies_by_country')
        return driver

    def GetData(self):
        href = dri