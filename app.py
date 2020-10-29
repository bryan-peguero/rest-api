from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/products')
def getProducts():
    return jsonify(products)

#Find/Obtain a Product
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        return jsonify({'product founded': productFound[0]})
    return jsonify({'message': 'Not Found'})

#POST a product
@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {"name": request.json['name'], 
    "price": request.json['price'],
    "description": request.json['description'],
    "stock": request.json['stock'] 
    }
    products.append(new_product)
    return jsonify({'message': 'Product added succesfully :D', 'products': products})

#PUT a product
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['description'] = request.json['description']
        productFound[0]['stock'] = request.json['stock']
        
        return jsonify({
            'message': 'Product updated',
            'product updated': productFound[0]
        })
    return 'Not Found'

#DELETE a product
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        products.remove(productFound[0])
        return jsonify({'message': 'The product was founded and deleted'})
    return 'Not Found'
#Init
if __name__ == '__main__':
    app.run(debug=True, port='5500')

