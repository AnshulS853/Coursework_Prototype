import sqlite3
from gettersetter import data

class databasefunction:
    def insertuserinfo(self,user_info):
        x = data()
        userID = x.get_userID()
        conn = sqlite3.connect("auc_database.db")
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO users
            (firstname,lastname,email,dob,gender)
            VALUES (?,?,?,?,?)
            WHERE userID = (?)
        ''',(user_info,userID))
        conn.commit()
        conn.close()


    def insertaddress(self,address):
        x = data()
        userID = x.get_userID()
        conn = sqlite3.connect("auc_database.db")
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO address
            (address1,address2,postcode,county)
            VALUES (?,?,?,?)
            WHERE userID = (?)
            ''',(address,userID))
        conn.commit()
        conn.close()