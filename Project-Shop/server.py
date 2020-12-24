from ProjectShop import projectShop
from flask import Flask, url_for, request, redirect, abort, jsonify
from flask_cors import CORS
app = Flask(__name__, static_url_path='', static_folder='staticpages')
CORS(app)
@app.route('/')
def index():
    return "hello"
#**************************************************************************************
#                                 SHOP
#**************************************************************************************
#get all Shop Products
@app.route('/Shop')
def getAllProducts():
    return jsonify(projectShop.getAllShop())

# find By id
@app.route('/Shop/<product>')
def findByName(product):
    return jsonify(projectShop.findByName(product))

# create
# curl -X POST -d "{\"product\":\"coke\", \"price\":123}" -H Content-Type:application/json http://127.0.0.1:5000/Shop
@app.route('/Shop', methods=['POST'])
def createProduct():
    if not request.json:
        abort(400)
    
    product = {
        "product": request.json["product"],
        "price": request.json["price"]
    }
    return jsonify(projectShop.createShop(product))


#update
#curl -X PUT -d "{\"product\":\"coke\", \"price\":999}" -H Content-Type:application/json http://127.0.0.1:5000/Shop/coke
@app.route('/Shop/<product>', methods=['PUT'])
def updateProductPrice(product):
    foundProducts= projectShop.findByName(product)
    if foundProducts == {}:
        return jsonify({}), 404
    
    currentProduct = foundProducts
    if 'product' in request.json:
        currentProduct['product'] = request.json['product']

    if 'price' in request.json:
        currentProduct['price'] = request.json['price']
    projectShop.updatePrice(currentProduct)
    return jsonify(currentProduct)

#delete
#curl -X DELETE http://127.0.0.1:5000/Shop/coke
@app.route('/Shop/<product>', methods=['DELETE'])
def deleteProduct(product):
    projectShop.deleteShopProduct(product)
    return jsonify({"done":True})

#**************************************************************************************
#                                 SHOPPING LIST
#**************************************************************************************
@app.route('/Shoppinglist')
def getShoppingList():
    return jsonify(projectShop.getShoppingList())

@app.route('/ShoppinglistTotal')
def getShoppingListTotal():
    return jsonify(projectShop.calculateTotal())

# find By id
@app.route('/Shoppinglist/<product>')
def findByListName(product):
    return jsonify(projectShop.findByListName(product))
# create
# curl -X POST -d "{\"product\":\"coke\", \"quantity\":5}" -H Content-Type:application/json http://127.0.0.1:5000/Shoppinglist
@app.route('/Shoppinglist', methods=['POST'])
def createShoppingList():
    if not request.json:
        abort(400)
    
    product = {
        "product": request.json["product"],
        "quantity": request.json["quantity"],
        "price": request.json["price"]
    }
    return jsonify(projectShop.createShoppingList(product))

#update Quantity
#curl -X PUT -d "{\"product\":\"coke\", \"quantity\":1}" -H Content-Type:application/json http://127.0.0.1:5000/Shoppinglist/coke
@app.route('/Shoppinglist/<product>', methods=['PUT'])
def updateQuantity(product):
    foundProducts= projectShop.findShoppingList(product)
    if foundProducts == {}:
        return jsonify({}), 404
    currentProduct = foundProducts
    if 'product' in request.json:
        currentProduct['product'] = request.json['product']
    if 'quantity' in request.json:
        currentProduct['quantity'] = request.json['quantity']
    projectShop.updateQuantity(currentProduct)
    return jsonify(currentProduct)
    

@app.route('/ShoppinglistPrice/<product>', methods=['PUT'])
def updateShoppingListPrice(product):
    foundProducts= projectShop.findShoppingList(product)
    if foundProducts == {}:
        return jsonify({}), 404

    currentProduct = foundProducts
    if 'product' in request.json:
        currentProduct['product'] = request.json['product']

    if 'price' in request.json:
        currentProduct['price'] = request.json['price']
    projectShop.updatePrice2(currentProduct)
    return jsonify(currentProduct)

# find By id
@app.route('/Shoppinglist/<product>')
def findShoppingList(product):
    return jsonify(projectShop.findShoppingList(product))

#delete
#curl -X DELETE http://127.0.0.1:5000/Shoppinglist/coke
@app.route('/Shoppinglist/<product>', methods=['DELETE'])
def deleteItem(product):
    projectShop.deleteItem(product)
    return jsonify({"done":True})
#**************************************************************************************
#                                 MAIN
#**************************************************************************************
if __name__ == "__main__":
    app.run(debug=True)