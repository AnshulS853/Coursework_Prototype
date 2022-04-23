import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

from datetime import datetime, timedelta

from databasefunction import databaseClass
import sqlite3
import locale

class auctionBids(QDialog):
    def __init__(self, app, bID, lID, admin, postcode):
        super(auctionBids, self).__init__()
        loadUi("placebid.ui", self)
        # connecting buttons to functions when clicked
        self.app = app
        self.buyerID = bID
        self.admin = admin
        self.listingID = lID
        self.postcode = postcode

        self.result = None
        self.buyerBid = None
        self.bidDetails = None

        self.goback.clicked.connect(self.gobackpage)
        self.continuepage.clicked.connect(self.confirmbid)

        self.conn = sqlite3.connect("auc_database.db",isolation_level=None)
        self.cur = self.conn.cursor()

        self.fillFields()

    def gobackpage(self):
        self.close()
        self.app.callViewListings(self.buyerID,self.admin)

    def checkprice(self, price):
        try:
            price = float(price)
            locale.setlocale(locale.LC_ALL, 'en_GB')
            price = locale.currency(price, grouping=True)
            return price
        except:
            self.confirmtoast.setText("Price must in a valid format")
            return

    def pricetoint(self,raw_price):
        locale.setlocale(locale.LC_ALL, 'en_GB')
        conv = locale.localeconv()
        raw_numbers = raw_price.strip(conv['currency_symbol'])
        amount = locale.atof(raw_numbers)
        return amount

    def validatebid(self):
        buyerBid = float(self.biddingfield.text())
        self.buyerBid = self.checkprice(buyerBid)
        if self.bidDetails is None:
            bidPrice = float(self.pricetoint(self.result[7]))
        else:
            bidPrice = float(self.pricetoint(self.bidDetails[0]))

        if buyerBid > bidPrice:
            return True
        else:
            self.confirmtoast.setText("Invalid Bid.\nMust be greater\nthan highest bid")
            return

    def confirmbid(self):
        if self.validatebid() is True:
            self.continuepage.setText("Confirm")
            self.confirmtoast.setText("Confirm your bid\nplacement of\n"+str(self.buyerBid))
            self.continuepage.clicked.connect(self.saveBid)

    def calculatedatediff(self):
        now = datetime.now().date()
        date = datetime.strptime(self.result[6], '%Y-%m-%d').date()

        difference = date - now

        years = difference.days // 365
        months = (difference.days - years * 365) // 30
        days = (difference.days - years * 365 - months * 30)

        remainingduration = (str(years)+" Years\n"+str(months)+" Months\n"+str(days)+" Days\n")
        return remainingduration

    def fetchdeliverylocation(self):
        self.cur.execute('SELECT addressID from usad WHERE userID = ?',(self.result[10],))
        addressID = self.cur.fetchall()
        addressID = addressID[0][0]
        self.cur.execute('SELECT postcode from address WHERE addressID = ?',(addressID,))
        postcode = self.cur.fetchall()
        postcode = postcode[0][0]
        return postcode

    def fillFields(self):
        self.confirmtoast.setText("")
        self.cur.execute('SELECT * FROM listings WHERE listingID = ?',(self.listingID,))
        self.result = self.cur.fetchall()
        self.result = self.result[0]

        self.titlefield.setText(self.result[1])

        remainingduration = self.calculatedatediff()
        self.durationfield.setText(str(remainingduration))
        self.deliveryfield.setText(self.result[8])
        self.deliverylocation.setText("Item is located near\n" + str(self.postcode))

        self.cur.execute('SELECT highestBid, bidDate FROM auctions WHERE listingID = ?', (self.listingID,))
        bidDetails = self.cur.fetchall()
        if bidDetails is None:
            self.highestbidfield.setText(str(self.result[7]))
        else:
            self.bidDetails = bidDetails[0]
            self.highestbidfield.setText(str(self.bidDetails[0]))
            self.bidtimefield.setText(str(self.bidDetails[1]))

    def saveBid(self):

        print("Bid saved successfully")
