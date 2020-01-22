from Dao.squads_dao import SquadsDao
from Model.squads import Squads
from Controller.frontend_controller import FrontController
from Controller.backend_controller import BackController

class SquadsController:
    dao = SquadsDao()
    backend_controller = BackController()
    frontend_controller = FrontController() 

    def listar_todos(self):
        return self.dao.listar_todos()

    def listar_por_id(self, id):
        return self.dao.listar_por_id(id)

    def salvar(self, squads:Squads):
        squads.lingbackend.id = self.backend_controller.salvar(squads.lingbackend) 
        squads.lingfrontend.id = self.frontend_controller.salvar(squads.lingfrontend)
        return self.dao.salvar(squads)

    def alterar(self, squads:Squads):
        self.dao.alterar(squads)

    def deletar(self, id):
        self.dao.deletar(id)
