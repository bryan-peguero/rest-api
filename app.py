from flask import Flask, jsonify

app = Flask(__name__)

from products import products

@app.route('/products')
def getProducts():
    return jsonify(products)

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    print(product_name)
    return 'congratulations'

#Init
if __name__ == "__main__":
    app.run(debug=True, port="5500")

