import sqlite3

class databaseClass:
    def __init__(self,uid):
        self.userID = uid
        self.conn = sqlite3.connect("auc_database.db",isolation_level=None)
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
        self.conn.close()

    def insertaddress(self,address):
        self.cur.execute('''
            INSERT INTO address
            (houseno,
            addfield1,
            addfield2,
            postcode,
            county)
            VALUES (?,?,?,?,?)
            ''', (address[0],address[1],address[2],address[3],address[4]))
        lastrow = self.cur.lastrowid
        self.conn.close()
        return lastrow

    def updateaddress(self,address):
        self.cur.execute('''
            UPDATE address
            SET houseno=?,
            addfield1=?,
            addfield2=?,
            postcode=?,
            county=?
            WHERE userID = (?)
            ''',(address[0],address[1],address[2],address[3],address[4],self.userID))
        self.conn.close()

    def insertlisting(self,listing):
        self.cur.execute('''
            INSERT INTO listings
            (title,
            description,
            category,
            condition,
            format,
            dateofend,
            price,
            delivery,
            active,
            sellerID)
            VALUES (?,?,?,?,?,?,?,?,?,?)
            ''',(listing[0],listing[1],listing[2],listing[3],listing[4],listing[5],listing[6],listing[7],listing[8],listing[9]))
        self.conn.close()

