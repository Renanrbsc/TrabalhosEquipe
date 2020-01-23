import sys
sys.path.append('C:/Users/900159/Documents/github renan/TrabalhosEquipe/Sistema_SQUADS')
sys.path.append('C:/Users/900145/Documents/TrabalhosEquipe/Sistema_SQUADS')
sys.path.append('C:/Users/Usuario/Documents/GitHub/TrabalhosEquipe/Sistema_SQUADS')
sys.path.append('C:/Users/900159/Documents/GitHub/TrabalhosEquipe/Sistema_SQUADS')
sys.path.append('C:/Users/900145/Documents/TrabalhosEquipe/Sistema_SQUADS')

from Controller.squads_controller import SquadsController
from Model.squads import Squads

def menu():
    print('*********************************')
    print('* 1- Listar por codigo de Squad *')
    print('* 2- Cadastrar Squad Dev        *')
    #print('* 3- Cadastrar Linguagem        * ')
    print('* 4- Alterar Squad Dev          *')
    print('* 5- Deletar Squad Dev          * # testando')
    print('*********************************')
    return int(input('* Digite a opcao: '))

controller = SquadsController()
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
    
    squad.name_squad = 'Homens de Cinza'
    squad.descricao = 'Smith'
    squad.numero_pessoas = 5
    squad.lingbackend.id = 1
    squad.lingfrontend.id = 1
    squad.lingsgbds.id = 1
    
    id_salvo = controller.salvar(squad)
    squad_dev = controller.listar_por_id(id_salvo)
    print(squad_dev)
    
# elif op == 3:
#     print('-----Cadastrar  Linguagens-----')
#     print('-----1-BACK 2-FRONT 3-SGBD-----')
#     op = int(input('Digite a opcao: '))

#     if op == 1:
#         squad.lingbackend.linguagembackend = input('Digite a linguagem BACKEND: ')
#         print(controller.salvar_back(squad))
#     elif op == 2:
#         squad.lingfrontend.linguagemfrontend = input('Digite a linguagem FRONTEND: ')
#         print(controller.salvar_front(squad))
#     elif op == 3:
#         squad.lingsgbds.nome_db = input('Digite a linguagem SGBD: ')
#         print(controller.salvar_sgbd(squad)) 

elif op == 4:
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


elif op == 5:
    print('-----Deletar Cliente-----')

    id = int(input('Informe o codigo do SQUAD_DEV: '))
    print(controller.listar_por_id(id))

    controller.deletar(id)
    
    print(controller.listar_por_id(id))

else:
    print('Estou perdido!')




