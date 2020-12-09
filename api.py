import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_AS_ASCII'] = False

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    { 'id': 0,
      'title': 'Parásito',
      'directed_by': 'Bong Joon-ho',
      'country': 'Corea del Sur',
      'year': '2019',
      'genre': 'Drama',
      'running_time': '132',
      'language': 'Coreano' },
    { 'id': 1,
      'title': 'Green Book: una amistad sin fronteras',
      'directed_by': 'Peter Farrelly',
      'country': 'Estados Unidos',
      'year': '2018',
      'genre': 'Biografía',
      'running_time': '130',
      'language': 'Inglés' },
    { 'id': 2,
      'title': 'La forma del agua',
      'directed_by': 'Guillermo del Toro',
      'country': 'Estados Unidos',
      'year': '2017',
      'genre': 'Fantasía',
      'running_time': '123',
      'language': 'Inglés' },
    { 'id': 3,
      'title': 'Luz de Luna',
      'directed_by': 'Barry Jenkins',
      'country': 'Estados Unidos',
      'year': '2016',
      'genre': 'Drama',
      'running_time': '111',
      'language': 'Inglés' },
    { 'id': 4,
      'title': 'En primera plana',
      'directed_by': 'Tom McCarthy',
      'country': 'Estados Unidos',
      'year': '2015',
      'genre': 'Drama',
      'running_time': '128',
      'language': 'Inglés' },
    # { 'id': -,
    #   'title': '',
    #   'directed_by': '',
    #   'country': '',
    #   'year': '',
    #   'genre': '',
    #   'running_time': '',
    #   'language': '' },
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Archivo Películas 2020</h1><p>Este sitio es un prototipo de API para las películas estrenadas en el 2020.</p>"


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/movies/all', methods=['GET'])
def api_all():
    return jsonify(books)


app.run()