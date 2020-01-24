from flask import Flask, render_template, request, redirect
import sys

sys.path.append(r'C:\Users\900159\Documents\TrabalhosEquipe\Sistema_SQUADS')
sys.path.append(r'C:\Users\900145\Documents\TrabalhosEquipe\Sistema_SQUADS')

from Controller.squads_controller import SquadsController
from Controller.backend_controller import BackController
from Controller.frontend_controller import FrontController
from Controller.sgbds_controller import SgbdsController
from Model.squads import Squads
from Model.backend import BackEnd
from Model.frontend import FrontEnd
from Model.sgbds import Sgbds

app = Flask(__name__)
squad = Squads()
back = BackEnd()
front = FrontEnd()
bd= Sgbds()
sqcontroller = SquadsController()
sgcontroller = SgbdsController()
bcontroller= BackController()
fcontroller = FrontController()
name = 'Sistema de Consulta Times de Desenvolvimento'

@app.route('/')
def inicio():
    return render_template('index.html',titulo_app = name)

@app.route('/listar')
def listar():
    return render_template('listar.html', titulo_app = name)

@app.route('/listar/codigo')
def editar():
    id = int(request.args['id'])
    squad = sqcontroller.listar_por_id(id)
    return render_template('listar_codigo.html', titulo_app = name, dados = squad)

@app.route('/listar/todos')
def listar_todos():
    squads = sqcontroller.listar_todos()

    return render_template('listar_todos.html', titulo_app = name, dados = squads)

@app.route('/listar/back')
def listar_back():
    back = bcontroller.listar_todos()
    return render_template('listar_back.html', titulo_app = name, dados = back)

@app.route('/listar/front')
def listar_front():
    front = fcontroller.listar_todos()
    return render_template('listar_front.html', titulo_app = name, dados = front)

@app.route('/listar/sgbd')
def listar_sgbd():
    sgbd = sgcontroller.listar_todos()
    return render_template('listar_sgbd.html', titulo_app = name, dados = sgbd)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', titulo_app = name)

@app.route('/cadastrar/squad')
def cadastrar_squad():
    return render_template('cadastrar_squad.html', titulo_app = name)

@app.route('/cadastrar/squad/inserir')
def cadastrado():
    squad.name_squad = request.args['nome']
    squad.descricao = request.args['desc']
    squad.numero_pessoas = int(request.args['integ'])
    squad.lingbackend.id = int(request.args['id_back'])
    squad.lingfrontend.id = int(request.args['id_front'])
    squad.lingsgbds.id = int(request.args['id_sgbd'])

    id_salvo = bcontroller.salvar(squad) 
    squad_dev = bcontroller.listar_por_id(id_salvo)

    return render_template('cadastrado.html', titulo_app = name, dados = squad_dev)

@app.route('/cadastrar/ling')
def cadastrar_linguagens():
    return render_template('cadastrar_ling.html', titulo_app = name)

@app.route('/cadastrar/linguagens')
def cadastrar_tipo_back():  
    ling = request.args['ling']    
    return render_template('cadastrar_linguagens.html', titulo_app = name, ling = ling)

@app.route('/cadastrar/ling/cadastrado')
def cadastrar_salvar():
    ling = request.args['ling']
    if ling == 'back':
        squad.lingbackend.linguagembackend = request.args['nome']
        dados = sqcontroller.salvar_back(squad)
    elif ling == 'front':
        squad.lingfrontend.linguagemfrontend = request.args['nome']
        dados = sqcontroller.salvar_front(squad)
    elif ling == 'banco':
        squad.lingsgbds.nome_db = request.args['nome']
        dados = sqcontroller.salvar_sgbd(squad)
    return render_template('cadastrado_ling_salvo.html', titulo_app = name, dados = dados)


@app.route('/alterar/squad')
def alterar():
    id = int(request.args['id'])
    id_squad = sqcontroller.listar_por_id(id)
    return render_template('alterar_id_squad.html', titulo_app = name,dados = id_squad, id = id)

@app.route('/alterar/linguagens')
def altera_lingua():
    pass

@app.route('/excluir/squad')
def excluir():
    id = int(request.args['id'])
    sqcontroller.deletar(id)
    return redirect('/listar/todos')

@app.route('/alterar/squad/atualizado')
def recebe_alterar_dados():
    id = int(request.args['id'])

    squad.name_squad = request.args['nome']
    squad.descricao = request.args['desc']
    squad.numero_pessoas = int(request.args['integ'])
    
    squad.lingbackend = int(request.args['id_back'])
    squad.lingfrontend = int(request.args['id_front'])
    squad.lingsgbds = int(request.args['id_sgbd'])

    sqcontroller.alterar(squad,id)

    tupla = sqcontroller.listar_por_id(id)
    return render_template('squad_atualizado.html',titulo_app = name, dados = tupla)

@app.route('/alterar/front')
def alterar_front():
    id = int(request.args['id'])
    tupla = fcontroller.listar_por_id(id)

    return render_template('alterar_front.html',titulo_app = name, dados = tupla, id= id)

@app.route('/alterar/front/dados')
def alterar_front_dados():
    id = int(request.args['id'])

    squad.lingfrontend.linguagemfrontend = request.args['nome']
    squad.lingfrontend.id = id
    fcontroller.alterar(squad)
    return redirect('/listar/front')

#@app.route('/excluir')
#def excluir():
#    id = int(request.args['id'])
#    controller.deletar(id)
#    if id_endereco != 'None':
#        endereco_controller.deletar(id_endereco)
#    return redirect('/listar')

app.run(debug=True)
