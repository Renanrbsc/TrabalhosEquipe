import sys
sys.path.append('C:/Users/900145/Documents/TrabalhosEquipe/Squads Lucas Berti e Renan')
sys.path.append('C:/Users/900145/Documents/TrabalhosEquipe/Squads Lucas Berti e Renan')
sys.path.append('C:/Users/900159/Documents/github renan/TrabalhosEquipe/Squads Lucas Berti e Renan')
sys.path.append('C:/Users/900159/Documents/GitHub/TrabalhosEquipe/Squads Lucas Berti e Renan')
sys.path.append('C:/Users/Usuario/Documents/GitHub/TrabalhosEquipe/Squads Lucas Berti e Renan')

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
    print('* 0- Listar todos os SQUADS     *')
    print('* 1- Listar por codigo de SQUAD *')
    print('* 2- Cadastrar SQUAD DEV        *')
    print('* 3- Alterar SQUAD DEV          *')
    print('* 4- Deletar SQUAD DEV          *')
    print('* 5- Cadastrar Linguagem        *')
    print('* 6- Alterar Linguagem          *')
    print('* 7- Deletar Linguagem          *')
    print('* 8- Listar todas Linguagem     *')
    print('*********************************')
    return int(input('* Digite a opcao: '))

controller = SquadsController()
controll_sgbd = SgbdsController()
controll_back = BackController()
controll_front = FrontController()

squad = Squads()

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
    
    squad.id_lingbackend = int(input('Digite a ID linguagem BACKEND: '))
    squad.id_lingfrontend = int(input('Digite a ID linguagem FRONTEND: '))
    squad.id_lingsgbds = int(input('Digite a ID linguagem SGBDS: '))

    controller.alterar(squad,id)

    tupla = controller.listar_por_id(id)
    print(tupla)

elif op == 4:
    print('-----Deletar Cliente-----')

    id = int(input('Informe o codigo do SQUAD_DEV: '))
    print(controller.listar_por_id(id))

    controller.deletar(id)
    print('Registro deletado!')
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

elif op == 7:
    print('-----Deletar  Linguagens-----')
    print('-----1-BACK 2-FRONT 3-SGBD-----')
    op = int(input('Digite a opcao: '))

    if op == 1:
        tupla = controll_back.listar_todos()
        for i in tupla:
            print(i)
        op = int(input('Digite a ID para deletar: '))
        controll_back.deletar(op)
        print('Registro deletado!')
        print(controll_back.listar_por_id(op))
    if op == 2:
        tupla = controll_front.listar_todos()
        for i in tupla:
            print(i)
        op = int(input('Digite a ID para deletar: '))
        controll_front.deletar(op)
        print('Registro deletado!')
        print(controll_front.listar_por_id(op))
    if op == 3:
        tupla = controll_sgbd.listar_todos()
        for i in tupla:
            print(i)
        op = int(input('Digite a ID para deletar: '))
        controll_sgbd.deletar(op)
        print('Registro deletado!')
        print(controll_sgbd.listar_por_id(op))

elif op == 8:
    print('------Listando  Linguagens------')
    controller.listar_ling()
    
else:
    print('Estou perdido!')




