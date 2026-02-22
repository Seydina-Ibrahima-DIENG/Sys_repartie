from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuration de la base de données (on utilise des variables d'environnement pour Docker plus tard)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://user:password@localhost:5432/mydb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modèle Utilisateur 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Modèle Produit 
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Route pour tester l'API 
@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price} for p in products])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # <--- Cette ligne crée les tables automatiquement
    app.run(host='0.0.0.0', port=5000)
