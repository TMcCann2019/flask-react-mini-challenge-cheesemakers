from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Producer(db.Model, SerializerMixin):
    __tablename__ = "producers"

    id = db.Column(db.Integer, primary_key=True)
    founding_year = db.Column(db.Integer)
    name = db.Column(db.String)
    region = db.Column(db.String)
    operation_size = db.Column(db.String)
    image = db.Column(db.String)

    @validates("founding_year")
    def validate_founding_year(self, key, value):
        if value is not None and value >= 1900:
            return value
        else:
            raise ValueError("Founding year must be greater than 1900")
        
    @validates("operation_size")
    def validate_operation_size(self, key, value):
        if "small" is value:
            return value
        elif "medium" is value:
            return value
        elif "large" is value:
            return value
        elif "family" is value:
            return value
        elif "corporate" is value:
            return value
        else:
            raise ValueError("Invalid operation size")

    def __repr__(self):
        return f"<Producer {self.id}>"


class Cheese(db.Model, SerializerMixin):
    __tablename__ = "cheeses"

    id = db.Column(db.Integer, primary_key=True)
    producer_id = db.Column(db.Integer, db.ForeignKey[Producer.id])
    kind = db.Column(db.String)
    is_raw_milk = db.Column(db.Boolean)
    production_date = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float)

    @validates("production_date")
    def validate_production_date(self, key, value):
        if value is not None and value <= "2024-02-23":
            return value
        else:
            raise ValueError("Production date must be before today")
        
    @validates("price")
    def validate_price(self, key, value):
        if value is not None and value >= 1.00 and value <= 45.00:
            return value
        else:
            raise ValueError("Price must be greater than 1.00 and less than 45.00")
        
    def __repr__(self):
        return f"<Cheese {self.id}>"
