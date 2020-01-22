from Dao.dao_backend import DaoBackEnd
from Model.backend import BackEnd

class BackController:
    dao = DaoBackEnd()

    def listar_todos(self):
        return self.dao.listar_todos()

    def listar_por_id(self, id):
        return self.dao.listar_por_id(id)

    def salvar(self, back:BackEnd):
        id = self.dao.salvar(back)
        return id

    def alterar(self, back:BackEnd, id):
        self.dao.alterar(back, id)

    def deletar(self, id):
        self.dao.deletar(id)
  