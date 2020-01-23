import sys
sys.path.append('C:/Users/900159/Documents/github renan/TrabalhosEquipe/Sistema_SQUADS')
sys.path.append('C:/Users/900145/Documents/TrabalhosSQL/Sistema_SQUADS')
sys.path.append('C:/Users/Usuario/Documents/GitHub/TrabalhosSQL/Sistema_SQUADS')

from Controller.squads_controller import SquadsController
from Model.squads import Squads

def menu():
    print('*********************************')
    print('* 1- Listar por codigo de Squad * #Comando funcionando')
    print('* 2- Cadastrar Squad Dev        * #Comando funcionando')
    print('* 3- Alterar Squad Dev          * # ')
    print('* 4- Deletar Squad Dev          * # ')
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
    
    squad.name_squad = 'Homens de BRANCO'
    squad.descricao = 'Smith'
    squad.numero_pessoas = 5
    squad.lingbackend.linguagembackend = 'Cobol'
    squad.lingfrontend.linguagemfrontend = 'HTML'
    squad.lingsgbds.nome_db = 'SQLite'
    
    id_salvo = controller.salvar(squad)
    squad_dev = controller.listar_por_id(id_salvo)
    print(squad_dev)
    
elif op == 3:
    print('-----Alterar Cliente-----')

    id = int(input('Informe o codigo do SQUAD_DEV: '))

    squad.name_squad = 'Homens de preto'
    squad.descricao = 'Smith'
    squad.numero_pessoas = 5
    squad.lingbackend.linguagembackend = 'Cobol'
    squad.lingfrontend.linguagemfrontend = 'HTML'
    squad.lingsgbds.nome_db = 'SQLite'

    print(controller.listar_por_id(id))
    id_salvo = controller.alterar(squad, id)

elif op == 4:
    print('-----Deletar Cliente-----')

    id = int(input('Informe o codigo do SQUAD_DEV: '))
    print(controller.listar_por_id(id))

    controller.deletar(id)

else:
    print('Estou perdido!')




