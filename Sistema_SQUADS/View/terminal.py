import sys
sys.path.append('C:/Users/900159/Documents/github renan/TrabalhosEquipe/Sistema_SQUADS')
sys.path.append('C:/Users/900145/Documents/TrabalhosEquipe/Sistema_SQUADS')
sys.path.append('C:/Users/Usuario/Documents/GitHub/TrabalhosEquipe/Sistema_SQUADS')
sys.path.append('C:/Users/900159/Documents/GitHub/TrabalhosEquipe/Sistema_SQUADS')
sys.path.append('C:/Users/900145/Documents/TrabalhosEquipe/Sistema_SQUADS')

from Controller.squads_controller import SquadsController
from Controller.sgbds_controller import SgbdsController
from Controller.backend_controller import BackController
from Controller.frontend_controller import FrontController

from Model.squads import Squads
from Model.sgbds import Sgbds
from Model.frontend import FrontEnd
from Model.backend import BackEnd

def menu():
    print('*********************************')
    print('* 1- Listar por codigo de Squad *')
    print('* 2- Cadastrar Squad Dev        *')
    print('* 3- Alterar Squad Dev          *')
    print('* 4- Deletar Squad Dev          * # testando')
    print('* 5- Cadastrar Linguagem        * ')
    print('* 6- Alterar Linguagem        * ')
    print('*********************************')
    return int(input('* Digite a opcao: '))

controller = SquadsController()
controll_sgbd = SgbdsController()
controll_back = BackController()
controll_front = FrontController()

squad = Squads()
sgbd = Sgbds()
back = BackEnd()
front = FrontEnd()

op = menu()
if op == 1:
    print('-----Busca por codigo-----')
    id = int(input('Digite o codigo: '))
    print(controller.listar_por_id(id))

    print('-----Listar todos-----')
    print(controller.listar_todos())

elif op == 2:
    print('-----Cadastrar SQUADS_DEV-----')
    
    squad.name_squad = input('Digite o nome do SQUAD: ')
    squad.descricao = input('Digite a descricao do SQUAD: ')
    squad.numero_pessoas = int(input('Digite o numero de integrantes do SQUAD: '))
    squad.lingbackend.id = int(input('Digite o ID DA linguagem BACKEND: '))
    squad.lingfrontend.id = int(input('Digite o ID DA linguagem FRONTEND: '))
    squad.lingsgbds.id = int(input('Digite o ID DA linguagem SGBD: '))
    
    id_salvo = controller.salvar(squad)
    squad_dev = controller.listar_por_id(id_salvo)
    print(squad_dev)

elif op == 3:
    print('-----Alterar SQUAD-LING-----')

    id = int(input('Informe o codigo do SQUAD_DEV: '))
    tupla = controller.listar_por_id(id)
    print(tupla)

    squad.name_squad = 'Homens de Preto'
    squad.descricao = 'llllllll'
    squad.numero_pessoas = 7
    
    squad.lingbackend = int(input('Digite a ID linguagem BACKEND: '))
    squad.lingfrontend = int(input('Digite a ID linguagem FRONTEND: '))
    squad.lingsgbds = int(input('Digite a ID linguagem SGBDS: '))

    controller.alterar(squad,id)

    tupla = controller.listar_por_id(id)
    print(tupla)

elif op == 4:
    print('-----Deletar Cliente-----')

    id = int(input('Informe o codigo do SQUAD_DEV: '))
    print(controller.listar_por_id(id))

    controller.deletar(id)

    print(controller.listar_por_id(id))
    
elif op == 5:
    print('-----Cadastrar  Linguagens-----')
    print('-----1-BACK 2-FRONT 3-SGBD-----')
    op = int(input('Digite a opcao: '))

    if op == 1:
        squad.lingbackend.linguagembackend = input('Digite a linguagem BACKEND: ')
        print(controller.salvar_back(squad))
    elif op == 2:
        squad.lingfrontend.linguagemfrontend = input('Digite a linguagem FRONTEND: ')
        print(controller.salvar_front(squad))
    elif op == 3:
        squad.lingsgbds.nome_db = input('Digite a linguagem SGBD: ')
        print(controller.salvar_sgbd(squad)) 

elif op == 6:
    print('-----Alterar  Linguagens-----')
    print('-----1-BACK 2-FRONT 3-SGBD-----')
    op = int(input('Digite a opcao: '))

    if op == 1:
        tupla = controll_back.listar_todos()
        for i in tupla:
            print(i)
        op = int(input('Digite a ID para alterar: '))
        squad.lingbackend.id = op
        squad.lingbackend.linguagembackend = input('Digite a linguagem BACKEND: ')
        controll_back.alterar(squad)
        print(controll_back.listar_por_id(op))
    if op == 2:
        tupla = controll_front.listar_todos()
        for i in tupla:
            print(i)
        op = int(input('Digite a ID para alterar: '))
        squad.lingfrontend.id = op
        squad.lingfrontend.linguagemfrontend = input('Digite a linguagem FRONTEND: ')
        controll_front.alterar(squad)
        print(controll_front.listar_por_id(op))
    if op == 3:
        tupla = controll_sgbd.listar_todos()
        for i in tupla:
            print(i)
        op = int(input('Digite a ID para alterar: '))
        squad.lingsgbds.id = op
        squad.lingsgbds.nome_db = input('Digite a linguagem SGBD: ')
        controll_sgbd.alterar(squad)
        print(controll_sgbd.listar_por_id(op))

else:
    print('Estou perdido!')




