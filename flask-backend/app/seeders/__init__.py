from flask.cli import AppGroup
from .seed_pokemons import seed_pokemons, unseed_pokemons
from .seed_items import seed_items, unseed_items


seed_cmd = AppGroup("seed")

@seed_cmd.command("all")
def seed_all():
  seed_pokemons()
  seed_items()

@seed_cmd.command("undo")
def seed_undo():
  unseed_pokemons()
  unseed_items()
