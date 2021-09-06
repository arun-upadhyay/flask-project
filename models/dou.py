import sqlite3
import os


class Dou:
    def __init__(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        dbPath = os.path.join(basedir, 'data.db')
        self.conn = sqlite3.connect(dbPath)

    def getDb(self):
        return self.conn
