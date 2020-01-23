from Dao.dao_sgbds import DaoSgbds
from Model.sgbds import Sgbds

class SgbdsController:
    dao = DaoSgbds()
    

    def listar_todos(self):
        return self.dao.listar_todos()

    def listar_por_id(self, id):
        return self.dao.listar_por_id(id)

    def salvar(self, db:Sgbds):
        return self.dao.salvar(db)
        
    def alterar(self, db:Sgbds):
        self.dao.alterar(db)

    def deletar(self, id):
        self.dao.deletar(id)
