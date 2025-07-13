#api pokemon 
import random
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data(poke_id):
    res = requests.get(f"{POKEAPI_URL}{poke_id}")
    if res.status_code != 200:
        return None
    data = res.json()
    return {
        "id": data["id"],
        "name": data["name"].capitalize(),
        "image": data["sprites"]["front_default"],
        "height": data["height"],
        "weight": data["weight"],
        "types": ", ".join(t["type"]["name"] for t in data["types"]),
        "base_experience": data["base_experience"],
        "abilities": ", ".join(a["ability"]["name"] for a in data["abilities"]),
        "hp": data["stats"][0]["base_stat"],
        "attack": data["stats"][1]["base_stat"],
        "defense": data["stats"][2]["base_stat"],
    }

@app.route("/", methods=["GET", "POST"])
def index():
    pokemons = []
    if request.method == "POST":
        ids = random.sample(range(1, 151), 9)
        pokemons = [get_pokemon_data(poke_id) for poke_id in ids if get_pokemon_data(poke_id)]
    return render_template("index.html", pokemons=pokemons)

if __name__ == "__main__":
    app.run(debug=True)
