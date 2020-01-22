import MySQLdb
from Model.frontend import FrontEnd

class DaoFrontEnd:
    conexao = MySQLdb.connect(host = '127.0.0.1',
                              database = 'PadawanHBSIS',
                              user = 'root')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando_sql = f"SELECT * FROM FRONTEND"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
        
    def listar_por_id(self,id):
        comando_sql = f"SELECT * FROM FRONTEND WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, frontend:FrontEnd):
        comando_sql = f"""INSERT INTO FRONTEND
        (
            LINGUAGEMFRONTEND           
        )
        VALUES
        (
            '{frontend.linguagemfrontend}'
        )"""
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, frontend:FrontEnd, id):
        comando_sql = f"""UPDATE FRONTEND
        SET 
            LINGUAGEMFRONTEND = '{frontend.linguagemfrontend}'
        WHERE ID = {frontend.id}
        """
        self.cursor.execute(comando_sql)
        self.conexao.commit()

    def deletar(self,id):
        comando_sql = f"DELETE FROM FRONTEND WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        

    

