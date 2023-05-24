from flask import Flask, make_response, request, jsonify # Primeiro é da onde está sendo importado, segundo é o que está sendo importado
from dataBase import Carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros', methods=['GET'])
def get_Carros():
    return make_response(jsonify(message='Lista de Carros',data=Carros))

@app.route("/carros", methods=["POST"])
def create_carro():
    NovoCarro = request.json
    Carros.append(NovoCarro)
    return make_response(jsonify(message='Carro Adicionado Com Sucesso!',data=NovoCarro))

app.run()