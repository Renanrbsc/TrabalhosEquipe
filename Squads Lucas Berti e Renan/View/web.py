#---------# Sys Path #---------#
from flask import Flask, render_template, request, redirect
import sys

#---------# Sys Path #---------#
sys.path.append(r'C:\Users\900159\Documents\TrabalhosEquipe\Sistema_SQUADS')
sys.path.append(r'C:\Users\900145\Documents\TrabalhosEquipe\Sistema_SQUADS')
#sys.path.append('C:/Users/900159/Documents/github renan/TrabalhosSQL/Aula36 17-01')
#sys.path.append('C:/Users/900145/Documents/TrabalhosEquipe/Squads Lucas Berti e Renan')
sys.path.append('C:/Users/Usuario/Documents/GitHub/TrabalhosSQL/Aula36 17-01')
sys.path.append(r'C:/Users/Usuario/Documents/GitHub/TrabalhosEquipe/Squads Lucas Berti e Renan')
sys.path.append(r'C:\Users\900159\Documents\GitHub\TrabalhosEquipe\Sistema_SQUADS')

#---------# Controllers #---------#
from Controller.squads_controller import SquadsController
from Controller.backend_controller import BackController
from Controller.frontend_controller import FrontController
from Controller.sgbds_controller import SgbdsController
from Model.squads import Squads
from Model.backend import BackEnd
from Model.frontend import FrontEnd
from Model.sgbds import Sgbds

#---------# Flask #---------#
app = Flask(__name__)

#---------# Models #---------#
squad = Squads()
back = BackEnd()
front = FrontEnd()
bd= Sgbds()

#---------# Controllers #---------#
sqcontroller = SquadsController()
sgcontroller = SgbdsController()
bcontroller= BackController()
fcontroller = FrontController()

#---------# Nome Website #---------#
name = 'Sistema de Consulta Times de Desenvolvimento'

@app.route('/')
def inicio():
    return render_template('index.html',titulo_app = name)

@app.route('/listar')
def listar():
    return render_template('listar.html', titulo_app = name)

@app.route('/listar/codigo')
def editar():
    id = request.args['id']
    if not id.isdigit():
        return redirect('/listar')
    squad = sqcontroller.listar_por_id(id)
    if squad == None:
        return redirect('/listar')
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
    dados_front = fcontroller.listar_todos()
    dados_back = bcontroller.listar_todos()
    dados_sgbd = sgcontroller.listar_todos()
    return render_template('cadastrar_squad.html', titulo_app = name,dados_front = dados_front,dados_back = dados_back,dados_sgbd = dados_sgbd)

@app.route('/cadastrar/squad/inserir')
def cadastrado():
    squad.name_squad = request.args['nome']
    squad.descricao = request.args['desc']
    squad.numero_pessoas = int(request.args['integ'])
    id_back = request.args['id_back'] # recebe valor html
    id_front = request.args['id_front'] # recebe valor html
    id_sgbd = request.args['id_sgbd']# recebe valor html
    if id_back == '' or id_front == '' or id_sgbd == '' or squad.name_squad == '' or squad.descricao == '' : # SE NULO redireciona a pagina
        return redirect('/cadastrar/squad')
    else:
        squad.lingbackend.id = int(id_back) # Se verdadeiro salva a id
        squad.lingfrontend.id = int(id_front) # Se verdadeiro salva a id
        squad.lingsgbds.id = int(id_sgbd) # Se verdadeiro salva a id

    id_salvo = sqcontroller.salvar(squad) # salva o dados no Banco de dados
    print(id_salvo)
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
    nome = request.args['nome']
    if nome == '':
        return render_template('cadastrar_linguagens.html', titulo_app = name, ling = ling)
    else:
        if ling == 'Backend':
            squad.lingbackend.linguagembackend = nome
            sqcontroller.salvar_back(squad)
            dados = bcontroller.listar_todos()
        elif ling == 'Frontend':
            squad.lingfrontend.linguagemfrontend = nome
            sqcontroller.salvar_front(squad)
            dados = fcontroller.listar_todos()
        elif ling == 'SGBD':
            squad.lingsgbds.nome_db = nome
            sqcontroller.salvar_sgbd(squad)
            dados = sgcontroller.listar_todos()
        return render_template('listar_linguagem.html', titulo_app = name,ling = ling, dados = dados)

@app.route('/alterar/squad')
def alterar():
    id = int(request.args['id'])
    id_squad = sqcontroller.listar_por_id(id)
    dados_front = fcontroller.listar_todos()
    dados_back = bcontroller.listar_todos()
    dados_sgbd = sgcontroller.listar_todos()    
    return render_template('alterar_id_squad.html', titulo_app = name,dados = id_squad, id = id,dados_front = dados_front,dados_back = dados_back,dados_sgbd = dados_sgbd)

@app.route('/excluir/squad')
def excluir_squad():
    id = int(request.args['id'])
    sqcontroller.deletar(id)
    return redirect('/listar/todos')

@app.route('/alterar/squad/atualizado')
def recebe_alterar_dados():
    id = int(request.args['id'])

    squad.name_squad = request.args['nome']
    squad.descricao = request.args['desc']
    squad.numero_pessoas = int(request.args['integ'])
    
    id_back = request.args['id_back'] # recebe valor html
    id_front = request.args['id_front'] # recebe valor html
    id_sgbd = request.args['id_sgbd']# recebe valor html
    if id_back == '' or id_front == '' or id_sgbd == '': # SE NULO redireciona a pagina
        id_squad = sqcontroller.listar_por_id(id)
        return render_template('alterar_id_squad.html', titulo_app = name,dados = id_squad, id = id)
    else:
        squad.id_lingbackend = int(id_back) # Se verdadeiro salva a id
        squad.id_lingfrontend = int(id_front) # Se verdadeiro salva a id
        squad.id_lingsgbds = int(id_sgbd) # Se verdadeiro salva a id

    sqcontroller.alterar(squad,id)
    tupla = sqcontroller.listar_por_id(id)
    return render_template('listar_codigo.html', titulo_app = name, dados = tupla)

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

@app.route('/excluir/linguagem')
def excluir_linguagem():
    id = int(request.args['id'])
    ling = request.args['ling']
    if ling == 'Backend':
        bcontroller.deletar(id)
        dados = bcontroller.listar_todos()
    if ling == 'Frontend':
        fcontroller.deletar(id)
        dados = fcontroller.listar_todos()
    if ling == 'SGBD':
        sgcontroller.deletar(id)
        dados = sgcontroller.listar_todos()
    return render_template('listar_linguagem.html', titulo_app = name, dados = dados,ling = ling)

app.run(debug=True)
