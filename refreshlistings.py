import sqlite3
from datetime import datetime

class refreshLists:
    def __init__(self,app):
        self.app = app
        self.conn = sqlite3.connect("auc_database.db", isolation_level=None)
        self.cur = self.conn.cursor()
        self.today = datetime.now().date()
        self.refreshall()

    def refreshall(self):
        self.cur.execute('SELECT listingID FROM listings WHERE dateofend=? AND active=1', (self.today,))
        result = self.cur.fetchall()

        insertlist = []

        for i in result:
            if i is not None:
                i = i[0]
                insertlist.append(i)

        self.updatedatabase(insertlist)

    def updatedatabase(self,list):
        for i in list:
            currentlistingID = i
            self.cur.execute('''
                            UPDATE listings
                            SET active=0
                            WHERE listingID = (?)
                            ''',(currentlistingID,))