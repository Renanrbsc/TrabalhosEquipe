from flask import Flask, render_template, request, redirect
import sys

sys.path.append(r'C:\Users\900159\Documents\TrabalhosEquipe\Sistema_SQUADS')
sys.path.append(r'C:\Users\900145\Documents\TrabalhosEquipe\Sistema_SQUADS')
#sys.path.append('C:/Users/900159/Documents/github renan/TrabalhosSQL/Aula36 17-01')
#sys.path.append('C:/Users/900145/Documents/TrabalhosEquipe/Sistema_SQUADS')
#sys.path.append('C:/Users/Usuario/Documents/GitHub/TrabalhosSQL/Aula36 17-01')
sys.path.append(r'C:/Users/Usuario/Documents/GitHub/TrabalhosEquipe/Sistema_SQUADS')
#sys.path.append('C:/Users/americo/Documents/Trabalhos python HBSis/TrabalhosEquipe/Sistema_SQUADS')

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

@app.route('/listar/linguagem')
def listar_front():
    ling = request.args['ling']   
    if ling == 'Frontend':
        dados = fcontroller.listar_todos()

    elif ling == 'Backend':
        dados = bcontroller.listar_todos()

    elif ling == 'SGBD':
        dados = sgcontroller.listar_todos()
    return render_template('listar_linguagem.html', titulo_app = name, dados = dados,ling = ling)

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

    id_salvo = sqcontroller.salvar(squad) 
    squad_dev = sqcontroller.listar_por_id(id_salvo)


    return render_template('listar_codigo.html', titulo_app = name,dados = squad_dev, id = id_salvo)

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
    if ling == 'Backend':
        squad.lingbackend.linguagembackend = request.args['nome']
        sqcontroller.salvar_back(squad)
        dados = bcontroller.listar_todos()
    elif ling == 'Frontend':
        squad.lingfrontend.linguagemfrontend = request.args['nome']
        sqcontroller.salvar_front(squad)
        dados = fcontroller.listar_todos()
    elif ling == 'SGBD':
        squad.lingsgbds.nome_db = request.args['nome']
        sqcontroller.salvar_sgbd(squad)
        dados = sgcontroller.listar_todos()
    return render_template('listar_linguagem.html', titulo_app = name,ling = ling, dados = dados)

@app.route('/alterar/squad')
def alterar():
    id = int(request.args['id'])
    id_squad = sqcontroller.listar_por_id(id)
    return render_template('alterar_id_squad.html', titulo_app = name,dados = id_squad, id = id)

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
    
    squad.id_lingbackend = int(request.args['id_back'])
    squad.id_lingfrontend = int(request.args['id_front'])
    squad.id_lingsgbds = int(request.args['id_sgbd'])

    sqcontroller.alterar(squad,id)

    tupla = sqcontroller.listar_por_id(id)
    return render_template('squad_atualizado.html',titulo_app = name, dados = tupla)

@app.route('/alterar/linguagem')
def alterar_front():
    id = int(request.args['id'])
    ling = request.args['ling']
    if ling == 'Frontend':
        tupla = fcontroller.listar_por_id(id)
    elif ling == 'Backend':
        tupla = bcontroller.listar_por_id(id)
    elif ling == 'SGBD':
        tupla = sgcontroller.listar_por_id(id)
    return render_template('alterar_linguagem.html',titulo_app = name, dados = tupla, id= id,ling = ling)

@app.route('/alterar/linguagem/dados')
def alterar_front_dados():
    id = int(request.args['id'])
    ling = request.args['ling']
    print(ling)
    if ling == 'Frontend':
        squad.lingfrontend.linguagemfrontend = request.args['nome']
        squad.lingfrontend.id = id
        fcontroller.alterar(squad)
    elif ling == 'Backend':
        squad.lingbackend.linguagembackend = request.args['nome']
        squad.lingbackend.id = id
        bcontroller.alterar(squad)
    elif ling == 'SGBD':
        squad.lingsgbds.nome_db = request.args['nome']
        squad.lingsgbds.id = id
        sgcontroller.alterar(squad)
    return redirect('/listar')

#@app.route('/excluir')
#def excluir():
#    id = int(request.args['id'])
#    controller.deletar(id)
#    if id_endereco != 'None':
#        endereco_controller.deletar(id_endereco)
#    return redirect('/listar')

app.run(debug=True)
