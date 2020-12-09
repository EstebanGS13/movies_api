import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Archivo Películas 2020</h1><p>Este sitio es un prototipo de API para las películas estrenadas en el 2020.</p>"

app.run()