import sqlite3

class databaseclass:
    def __init__(self,uid):
        self.userID = uid

    def insertuserinfo(self,user_info):
        conn = sqlite3.connect("auc_database.db")
        cur = conn.cursor()
        cur.execute('''
            UPDATE users
            SET firstname=?,
            lastname=?,
            email=?,
            dob=?,
            gender=?
            WHERE userID = (?)
        ''',(user_info[0],user_info[1],user_info[2],user_info[3],user_info[4],self.userID))
        conn.commit()
        conn.close()

    def insertaddress(self,address):
        conn = sqlite3.connect("auc_database.db")
        cur = conn.cursor()
        cur.execute('''
            UPDATE address
            SET address1=?,
            address2=?,
            postcode=?,
            county=?
            WHERE userID = (?)
            ''',(address[0],address[1],address[2],address[3],self.userID))
        conn.commit()
        conn.close()