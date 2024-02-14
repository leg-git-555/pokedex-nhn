from sqlalchemy.sql import text
from random import choice, randint
from faker import Faker
from ..models import db
from ..models.Item import Item


def seed_items():
    fake = Faker()
    images = [
        "/images/pokemon_berry.svg",
        "/images/pokemon_egg.svg",
        "/images/pokemon_potion.svg",
        "/images/pokemon_super_potion.svg",
    ]
    items = []

    for i in range(10):
        items.append({
            "pokemon_id": i+1,
            "name": fake.name(),
            "price": randint(1, 100),
            "happiness": randint(1, 100),
            "image_url": choice(images)
        })

    for item in items:
        db.session.add(Item(**item))
        db.session.commit()


def unseed_items():
    db.session.execute(text("DELETE FROM items"))
    db.session.commit()
