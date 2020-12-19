from ProjectShop import projectShop

product1 = {
    'product': "Bread",
    'price' : 0.70,
}

product2 = {
    'product': "Coke Can",
    'price' : 1.10,
}
product3 = {
    'product': "Bread",
    'price' : 0.96,
}

item1={
    "product":"Coke Can",
    "quantity":2
}
item2={
    "product":"Bread",
    "quantity":2
}
item3={
    "product":"Coke Can",
    "quantity":4
}

#returnvalue = projectShop.createShop(product1)
#returnvalue = projectShop.createShop(product2)
#returnvalue = projectShop.createShoppingList(item1)
#returnvalue = projectShop.createShoppingList(item2)
print("**** GET ALL ****")
#returnvalue = projectShop.getAllShop()
returnvalue = projectShop.getShoppingList()
print(returnvalue)
print("\n**** FIND BY NAME ****")
#returnvalue = projectShop.findByName(product3['product'])
#returnvalue = projectShop.findByName(item3['product'])
#print(returnvalue)
print("\n**** UPDATE PRICE ****")
#returnvalue = projectShop.updatePrice(product3)
returnvalue = projectShop.updateQuantity(item3)
print(returnvalue)
print("\n**** DELETE PRODUCT ****")
#returnvalue = projectShop.deleteShopProduct(product3["product"])
returnvalue = projectShop.deleteItem(item3["product"])
print(returnvalue)