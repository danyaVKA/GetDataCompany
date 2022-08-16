# -*- coding: utf-8 -*-

import sqlite3

class write_data:
    def __init__(self):
        self.data = sqlite3.connect('InfoCompany.db')
        self.cursor = self.data.cursor()

    def create_table(self):
        self.cursor.execute("CREATE TABLE InfoCompany (Country message_text, ID integer, Company message_text , Industry message_text , Sector message_text )")

    def insert_table(self, ID, Country, Company, Industry, Sector):
        self.cursor.execute(
            "INSERT INTO InfoCompany (Country, ID, Company, Industry, Sector) VALUES (?, ?, ?, ?, ?)", (Country, ID, Company, Industry, Sector))
        self.data.commit()

    def show_database(self):
        for row in self.cursor.execute("SELECT * FROM  InfoCompany"):
            print(row)


    def drop_table(self):
        self.cursor.execute("DROP TABLE InfoCompany")
        #self.cursor.execute("DELETE FROM InfoCompany")

    def exist(self):
        self.cursor.close()



DB = write_data()
#DB.create_table()
#DB.insert_table(1, 'Russia', 'Gazprom', 'Gaz', 'Extraction')
DB.show_database()
#DB.drop_table()