import sqlite3

conn = sqlite3.connect("auc_database.db")
cur = conn.cursor()

from CreateAccount import signupfunction

def insertuserinfo(user_info):
    cur.execute('''
        INSERT INTO users
        (firstname,lastname,email,dob,gender)
        VALUES (?,?,?,?,?)
        WHERE username = (?)
    ''',(user_info,username))


def insertgender(gender,userID):
    cur.execute('''
                UPDATE users
                SET gender=?,
                WHERE userID=?
                ''',(gender,userID))
    conn.commit()


def insertaddress(address,userID):
    cur.execute('''
        INSERT INTO address
        (address1,address2,postcode,county)
        VALUES (?,?,?,?)
        WHERE userID = (?)
        ''',(address,userID))
    conn.commit()

conn.close()