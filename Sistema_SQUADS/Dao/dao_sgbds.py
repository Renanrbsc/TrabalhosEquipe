import MySQLdb
from Model.sgbds import Sgbds

class DaoSgbds:
    conexao = MySQLdb.connect(host = '127.0.0.1',
                              database = 'PadawanHBSIS',
                              user = 'root')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando_sql = f"SELECT * FROM SGBDS"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
        
    def listar_por_id(self,id):
        comando_sql = f"SELECT * FROM SGBDS WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, db:Sgbds):
        comando_sql = f"""INSERT INTO SGBDS
        (
            NOME_DB           
        )
        VALUES
        (
            '{db.nome_db}'
        )"""
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, db:Sgbds):
        comando_sql = f"""UPDATE SGBDS
        SET 
            NOME_DB = '{db.nome_db}'
        WHERE ID = {db.id}
        """
        self.cursor.execute(comando_sql)
        self.conexao.commit()

    def deletar(self,id):
        comando_sql = f"DELETE FROM SGBDS WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        

    

