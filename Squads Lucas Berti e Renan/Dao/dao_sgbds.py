import MySQLdb
from Model.sgbds import Sgbds

class DaoSgbds:
    conexao = MySQLdb.connect(host = 'mysql.padawans.dev',
                              database = 'padawans16',
                              user = 'padawans16',
                              passwd = 'lr2019')
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
    
    def listar_codigo(self,id):
        comando_sql = f"SELECT ID FROM SGBDS WHERE ID = {id}"
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
            NOME_DB = '{db.lingsgbds.nome_db}'
        WHERE ID = {db.lingsgbds.id}
        """
        self.cursor.execute(comando_sql)
        self.conexao.commit()

    def deletar(self,id):
        comando_sql = f"DELETE FROM SGBDS WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        

    

