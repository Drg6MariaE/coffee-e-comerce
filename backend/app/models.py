from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_premium = db.Column(db.Boolean, default=False) # For Subscriptions
    
    # Relationships
    wishlist = db.relationship('Product', secondary='wishlist')

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(255))
    
    # Specific Coffee Attributes
    roast_level = db.Column(db.String(50)) # e.g., Light, Medium, Dark
    grind_option = db.Column(db.String(50)) # e.g., Whole Bean, Drip, Espresso

# Many-to-Many Table for Wishlist
wishlist = db.Table('wishlist',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True)
)