from flask import Blueprint, request, redirect
from ..models import Pokemon

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/pokemon")
def pokemons():
  return [pokemon.to_dict_all() for pokemon in Pokemon.query.all()]


@bp.route("/pokemon/<int:id>")
def pokemon_details(id):
  return Pokemon.query.get(id).to_dict_one()


"""
router.post(
  '/',
  pokemonValidations.validateCreate,
  asyncHandler(async function (req, res) {
    const id = await PokemonRepository.create(req.body);
    return res.redirect(`${req.baseUrl}/${id}`);
  })
);
"""
@bp.route("/pokemon", methods=['POST'])
def new_pokemon():
  data = request.json
  data['image_url'] = data['imageUrl']
  del data['imageUrl']
  del data['move1']
  del data['move2']
  print(data,'🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼')
  pokemon = Pokemon(**data)
  print(pokemon)
  return redirect(f"/api/pokemon/{id}")


@bp.route("/pokemons/<int:id>", methods=['PUT'])
def edit_pokemon():
  pass


@bp.route("/pokemons/types")
def pokemon_types():
  pass


@bp.route("/pokemons/random")
def random_pokemons():
  pass


@bp.route("/pokemons/battle")
def battle_pokemons():
  pass


@bp.route("/pokemons/<int:id>/items")
def pokemon_items():
  pass


@bp.route("/pokemons/<int:id>/items", methods=['POST'])
def new_item():
  pass


@bp.route("/items/<int:id>", methods=['PUT'])
def edit_item():
  pass


@bp.route("/items/<int:id>", methods=['DELETE'])
def delete_item():
  pass
