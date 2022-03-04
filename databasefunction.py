import sqlite3

class databaseClass:
    def __init__(self,uid):
        self.userID = uid
        self.conn = sqlite3.connect("auc_database.db")
        self.cur = self.conn.cursor()

    def insertuserinfo(self,user_info):
        self.cur.execute('''
            UPDATE users
            SET firstname=?,
            lastname=?,
            email=?,
            dob=?,
            gender=?
            WHERE userID = (?)
        ''',(user_info[0],user_info[1],user_info[2],user_info[3],user_info[4],self.userID))
        self.conn.commit()
        self.conn.close()


    def insertaddress(self,address):
        self.cur.execute('''
            UPDATE address
            SET address1=?,
            address2=?,
            postcode=?,
            county=?
            WHERE userID = (?)
            ''',(address[0],address[1],address[2],address[3],self.userID))
        self.conn.commit()
        self.conn.close()
