from flask import Flask, jsonify

app = Flask(__name__)

from products import products

@app.route('/products')
def getProducts():
    return jsonify(products)

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        return jsonify({'product founded': productFound[0]})
    return jsonify({'message': 'Not Found'})

@app.route('/products', methods=['POST'])
def addProduct():
    return jsonify({'message':'it works'})

#Init
if __name__ == '__main__':
    app.run(debug=True, port='5500')

