from Dao.squads_dao import SquadsDao
from Model.squads import Squads
from Controller.frontend_controller import FrontController
from Controller.backend_controller import BackController
from Controller.sgbds_controller import SgbdsController

class SquadsController:
    dao = SquadsDao()
    backend_controller = BackController()
    frontend_controller = FrontController()
    sgbds_controller = SgbdsController()

    def listar_todos(self):
        return self.dao.listar_todos()

    def listar_por_id(self, id):
        return self.dao.listar_por_id(id)

    def listar_ling(self):
        ling = []
        lista = ['BACKEND','FRONTEND','SGBD']
        ling.append(self.backend_controller.listar_todos())
        ling.append(self.frontend_controller.listar_todos())
        ling.append(self.sgbds_controller.listar_todos())
        for i in range(3):
            print(f'{lista[i]} - {ling[i]}')

    def salvar(self, squads:Squads):
        return self.dao.salvar(squads)

    def salvar_back(self, squads:Squads):
        if squads.lingbackend.linguagembackend == '':
            print('Dados não informados!')
        else:
            id = self.backend_controller.salvar(squads.lingbackend)

            return self.backend_controller.listar_por_id(id)

    def salvar_front(self, squads:Squads):
        if squads.lingfrontend.linguagemfrontend == '':
            print('Dados não informados!')
        else:
            id = self.frontend_controller.salvar(squads.lingfrontend)

            return self.frontend_controller.listar_por_id(id)

    def salvar_sgbd(self, squads:Squads):
        if squads.lingsgbds.nome_db == '':
            print('Dados não informados!')
        else:
            id = self.sgbds_controller.salvar(squads.lingsgbds)

            return self.sgbds_controller.listar_por_id(id)

    def alterar(self, squads:Squads, id):

        self.dao.alterar(squads, id)

    def deletar(self, id):
        self.dao.deletar(id)
