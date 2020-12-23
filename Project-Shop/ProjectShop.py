import mysql.connector
import dbconfig as cfg
from mysql.connector import cursor

class ProjectShop:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql['host'],
            user= cfg.mysql['username'],
            password = cfg.mysql['password'],
            database =cfg.mysql['database']
        )
    #**************************************************************************************
    #                   SHOP PRODUCT FUNCTIONS
    #**************************************************************************************
    def createShop(self, product):
        cursor = self.db.cursor()
        sql = "insert into shop (product, price) values (%s,%s)"
        values = [
            product['product'],
            product['price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid

    def getAllShop(self):
        cursor = self.db.cursor()
        sql = 'select * from shop'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToShopDict(result)
            returnArray.append(resultAsDict)
        cursor.close()
        return returnArray


    def findByName(self, product):
        cursor = self.db.cursor()
        sql = 'select * from shop where product = %s'
        values = [ product ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToShopDict(result)

    def updatePrice(self, product):
       cursor = self.db.cursor()
       sql = "update shop set price = %s where product = %s"
       values = [
           product['price'],
           product['product']
       ]
       cursor.execute(sql, values)
       self.db.commit()
       cursor.close()
       return product

    def deleteShopProduct(self, product):
       cursor = self.db.cursor()
       sql = "delete from shop where product= %s"
       values = [
           product
        ]
       cursor.execute(sql,values)
       self.db.commit()
       cursor.close()
       return product

    def convertToShopDict(self, result):
        colnames = ['id','product','price']
        product = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                product[colName] = value
        return product

    #**************************************************************************************
    #                   CUSTOMER FUNCTIONS
    #**************************************************************************************
    def createShoppingList(self, product):
        cursor = self.db.cursor()
        sql = "insert into customer (product, quantity,price) values (%s,%s,%s)"
        values = [
            product['product'],
            product['quantity'],
            product['price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return cursor.lastrowid

    def findByListName(self, product):
        cursor = self.db.cursor()
        sql = 'select * from customer where product = %s'
        values = [ product ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToCustomerDict(result)

    def getShoppingList(self):
        cursor = self.db.cursor()
        sql = 'select * from customer'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToCustomerDict(result)
            returnArray.append(resultAsDict)
        cursor.close()
        return returnArray

    def updateQuantity(self, product):
       cursor = self.db.cursor()
       sql = "update customer set quantity = %s where product = %s"
       values = [
           product['quantity'],
           product['product']
       ]
       cursor.execute(sql, values)
       self.db.commit()
       cursor.close()
       return product

    def updatePrice2(self, product):
       cursor = self.db.cursor()
       sql = "update customer set price = %s where product = %s"
       values = [
           product['price'],
           product['product']
       ]
       cursor.execute(sql, values)
       self.db.commit()
       cursor.close()
       return product

    def deleteItem(self, product):
       cursor = self.db.cursor()
       sql = "delete from customer where product= %s"
       values = [
           product
        ]
       cursor.execute(sql,values)
       self.db.commit()
       cursor.close()
       return product

    def findShoppingList(self, product):
        cursor = self.db.cursor()
        sql = 'select * from customer where product = %s'
        values = [ product ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToCustomerDict(result)

    def convertToCustomerDict(self, result):
        colnames = ['id','product','quantity','price']
        product = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                product[colName] = value
            return product
        else:
            return 1

    def convertToTotalDict(self, result):
        colnames = ['quantity','price']
        product = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                product[colName] = value
            return product
        else:
            return 1

    def calculateTotal(self):
        cursor = self.db.cursor()
        sql = 'select quantity,price from customer'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToTotalDict(result)
            returnArray.append(resultAsDict)
        cursor.close()
        return returnArray


projectShop = ProjectShop()