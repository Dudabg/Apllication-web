from flask import Flask, request, jsonify
from models import Product


app = Flask(__name__)


@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    new_product = Product(name=data['name'], description=data['description'], price=data['price'])
    new_product.save()  # Supondo que você tenha um método 'save()' na classe Product para salvar no banco de dados
    return jsonify({'message': 'Product created successfully'}), 201



@app.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()  # Supondo que você tenha um método 'query.all()' na classe Product para buscar todos os produtos
    output = []
    for product in products:
        product_data = {'id': product.id, 'name': product.name, 'description': product.description, 'price': str(product.price)}
        output.append(product_data)
    return jsonify({'products': output})



@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)  # Supondo que você tenha um método 'query.get()' na classe Product para buscar um produto por ID
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    product_data = {'id': product.id, 'name': product.name, 'description': product.description, 'price': str(product.price)}
    return jsonify({'product': product_data})



@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    data = request.json
    product.name = data['name']
    product.description = data['description']
    product.price = data['price']
    product.save()  # Supondo que você tenha um método 'save()' na classe Product para atualizar no banco de dados
    return jsonify({'message': 'Product updated successfully'})



@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    product.delete()  # Supondo que você tenha um método 'delete()' na classe Product para deletar no banco de dados
    return jsonify({'message': 'Product deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
