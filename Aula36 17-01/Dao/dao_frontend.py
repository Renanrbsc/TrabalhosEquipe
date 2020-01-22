import MySQLdb
from Model.frontend import FrontEnd

class FrontEnd:
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
            LINGUAGEMBACKEND           
        )
        VALUES
        (
            '{frontend.}'
        )"""
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, frontend:FrontEnd, id):
        comando_sql = f"""UPDATE FRONTEND
        SET 
            NAME_SQUAD = '{squads.name_squad}',
            DESCRICAO = '{squads.descricao}',
            NUMERO_PESSOAS = {squads.numero_pessoas},
            LINGUAGEMBACKEND = '{squads.linguagembackend}',
            LINGUAGEMFRONTEND = '{squads.linguagemfrontend}'
        WHERE ID = {id}
        """
        self.cursor.execute(comando_sql)
        self.conexao.commit()

    def deletar(self,id):
        comando_sql = f"DELETE FROM FRONTEND WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        

    
