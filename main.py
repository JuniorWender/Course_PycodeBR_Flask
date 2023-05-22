from flask import Flask, make_response, request, jsonify # Primeiro é da onde está sendo importado, segundo é o que está sendo importado
from dataBase import Carros

app = Flask(__name__)

@app.route("/carros", methods=["GET"])
def get_carros():
    return make_response(jsonify(Carros))

@app.route("/carros", methods=["POST"])
def create_carro():
    NovoCarro = request.json
    Carros.append(NovoCarro)
    return NovoCarro


app.run()