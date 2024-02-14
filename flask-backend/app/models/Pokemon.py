from .db import db
from datetime import datetime

class Pokemon(db.Model):
  __tablename__ = 'pokemons'
  id = db.Column(db.Integer, primary_key=True, allow_null=False)
  number = db.Column(db.Integer, allow_null=False, unique=True)
  attack = db.Column(db.Integer, allow_null=False)
  defense = db.Column(db.Integer, allow_null=False)
  imageUrl = db.Column(db.String(255), allow_null=False)
  name = db.Column(db.String(255), allow_null=False, unique=True)
  type = db.Column(db.String, allow_null=False)
  moves = db.Column(db.String(255), allow_null=False)
  encounterRate = db.Column(db.Decimal, allow_null=False, default=1.00)
  catchRate = db.Column(db.Decimal, allow_null=False, default=1.00)
  captured = db.Column(db.Boolean, allow_null=False,  default=False)
  created_at = db.Column(db.Date, default=datetime.now)
  updated_at = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)