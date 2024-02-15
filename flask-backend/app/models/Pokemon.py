from .db import db
from datetime import datetime

class Pokemon(db.Model):
    __tablename__ = 'pokemons'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    number = db.Column(db.Integer, nullable=False, unique=True)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    type = db.Column(db.String, nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encounter_rate = db.Column(db.Float(3, 2), nullable=False, default=1.00)
    catch_rate = db.Column(db.Float(3, 2), nullable=False, default=1.00)
    captured = db.Column(db.Boolean, nullable=False,  default=False)
    created_at = db.Column(db.Date, default=datetime.now)
    updated_at = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)

    items = db.relationship("Item", back_populates="pokemon", cascade="all, delete-orphan")

    def to_dict_all(self):
        return {
            "id": self.id,
            "imageUrl": self.image_url,
            "number": self.number,
            "name": self.name,
            "captured": self.captured
        }

    def to_dict_one(self):
        return {
            "imageUrl": self.image_url,
            "moves": self.moves.split(','),
            "id": self.id,
            "number": self.number,
            "attack": self.attack,
            "defense": self.defense,
            "name": self.name,
            "type": self.type,
            "captured": self.captured,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at
        }

    @classmethod
    def types():
        return [
            "fire",
            "electric",
            "normal",
            "ghost",
            "psychic",
            "water",
            "bug",
            "dragon",
            "grass",
            "fighting",
            "ice",
            "flying",
            "poison",
            "ground",
            "rock",
            "steel",
        ]
