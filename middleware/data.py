import sqlite3

class DataBase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

        """ Table commands """


    def add_data(self, photos, description):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO ads (photos, description) VALUES (?, ?)", (photos, description, ))