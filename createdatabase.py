import sqlite3 as sl3
import datetime
# from sqlite3 import Error
# from datetime import timedelta,date
# import sys

conn = sl3.connect("auc_database.db")

def setup_db():
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users 
                        ( userID    Integer PRIMARY KEY AUTOINCREMENT
                        , admin     Integer
                        , username  Text
                        , password  Integer
                        , firstname Text
                        , lastname  Text
                        , gender    Integer
                        , email     Text
                        , dob       Integer
                        );
                        
                CREATE TABLE IF NOT EXISTS listings 
                        ( listingID Integer PRIMARY KEY AUTOINCREMENT
                        );
                """)
    c.close
    print("Tables created successfully")

conn.close()