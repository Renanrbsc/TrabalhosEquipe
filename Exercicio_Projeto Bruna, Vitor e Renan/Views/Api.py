import sys
from flask_restful import Api
from flask import Flask

sys.path.append(r'C:\Users\900159\Documents\GitHub\TrabalhosEquipe\Exercicio_Projeto Bruna, Vitor e Renan')

from Controller.open_txt import ControllerAmigo
app = Flask(__name__)
api = Api(app)

api.add_resource(ControllerAmigo, '/amigo', endpoint='amigos')


app.run(debug=True)


