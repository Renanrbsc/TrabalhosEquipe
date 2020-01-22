from Dao.dao_backend import BackEnd
from Model.backend import backEnd

class BackController:
    dao = BackEnd()

    def listar_todos(self):
        return self.dao.listar_todos()

    def listar_por_id(self, id):
        return self.dao.listar_por_id(id)

    def salvar(self, back=BackEnd):
        id = self.dao.salvar(squads)
        return id

    def alterar(self, squads:Squads, id):
        self.dao.alterar(squads, id)

    def deletar(self, id):
        self.dao.deletar(id)
