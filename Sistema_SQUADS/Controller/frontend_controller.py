from Dao.dao_frontend import DaoFrontEnd
from Model.frontend import FrontEnd

class FrontController:
    dao = DaoFrontEnd()
    

    def listar_todos(self):
        return self.dao.listar_todos()

    def listar_por_id(self, id):
        return self.dao.listar_por_id(id)

    def salvar(self, front:FrontEnd):
        return self.dao.salvar(front)     

    def alterar(self, front:FrontEnd):
        self.dao.alterar(front)

    def deletar(self, id):
        self.dao.deletar(id)
