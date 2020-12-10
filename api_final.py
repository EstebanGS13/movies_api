import flask
from flask import request, jsonify
import sqlite3


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_AS_ASCII'] = False

# Create some test data for our catalog in the form of a list of dictionaries.
movies = [
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

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# http://127.0.0.1:5000/
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Archivo Películas 2010 - 2020</h1>
    <p>Este sitio es un prototipo de API para las películas estrenadas en la última década.</p>'''


# A route to return all of the available entries in our catalog.
# http://127.0.0.1:5000/api/v1/resources/movies/all
@app.route('/api/v1/resources/movies/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('movies.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_movies = cur.execute('SELECT * FROM movies;').fetchall()

    return jsonify(all_movies)


# http://127.0.0.1:5000/api/v1/resources/movies
@app.route('/api/v1/resources/movies', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id_ = query_parameters.get('id')
    title = query_parameters.get('title')
    directed_by = query_parameters.get('directed_by')
    country = query_parameters.get('country')
    year = query_parameters.get('year')
    genre = query_parameters.get('genre')
    running_time = query_parameters.get('running_time')
    language = query_parameters.get('language')

    query = "SELECT * FROM movies WHERE"
    to_filter = []

    if id_:
        query += ' id=? AND'
        to_filter.append(id_)
        print(id_)
    if title:
        query += ' title=? AND'
        to_filter.append(title)
    if directed_by:
        query += ' directed_by=? AND'
        to_filter.append(directed_by)
    if country:
        query += ' country=? AND'
        to_filter.append(country) 
    if year:
        query += ' year=? AND'
        to_filter.append(year)  
    if genre:
        query += ' genre=? AND'
        to_filter.append(genre)   
    if running_time:
        query += ' running_time=? AND'
        to_filter.append(running_time)
    if language:
        query += ' language=? AND'
        to_filter.append(language)
    if not (id_ or title or directed_by or country or year or genre or running_time or language):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('movies.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>No se encontró el recurso.</p>", 404


app.run()