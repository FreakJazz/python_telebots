from flask import Flask, render_template, request
import requests
import math

app = Flask(__name__)

MORTI_PER_PAGE = 9

@app.route('/', methods=['GET'])
def index():
    search_query = request.args.get('search', '').lower()
    page = int(request.args.get('page', 1))

    url = f'https://rickandmortyapi.com/api/character/?page={page}'
    response = requests.get(url)

    if response.status_code != 200:
        return "Error al obtener los personajes."

    data = response.json()
    all_characters = []

    for character in data['results']:
        name = character['name'].lower()

        if search_query in name:
            morti = {
                'id': character['id'],
                'name': character['name'],
                'status': character['status'],
                'species': character['species'],
                'type': character['type'] if character['type'] else 'Unknown',
                'gender': character['gender'],
                'origin': character['origin']['name'],
                'location': character['location']['name'],
                'image': character['image'],
                'episode_count': len(character['episode'])
            }
            all_characters.append(morti)

    total = data['info']['count']
    total_pages = data['info']['pages']

    return render_template('index.html', 
                           character_list=all_characters,
                           search_query=search_query,
                           page=page,
                           total_pages=total_pages)

if __name__ == '__main__':
    app.run(debug=True)
