import MySQLdb
from Model.backend import BackEnd

class DaoBackEnd:
    conexao = MySQLdb.connect(host = 'mysql.padawans.dev',
                              database = 'padawans16',
                              user = 'padawans16',
                              passwd = 'lr2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando_sql = f"SELECT * FROM BACKEND"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
        
    def listar_por_id(self,id):
        comando_sql = f"SELECT * FROM BACKEND WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, backend:BackEnd):
        comando_sql = f"""INSERT INTO BACKEND
        (
            LINGUAGEMBACKEND
        )
        VALUES
        (
            '{backend.linguagembackend}'
        )"""
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, backend:BackEnd):
        print(backend.linguagembackend)
        comando_sql = f"""UPDATE BACKEND
        SET 
            LINGUAGEMBACKEND = '{backend.linguagembackend}'
        WHERE ID = {backend.id}
        """
        self.cursor.execute(comando_sql)
        self.conexao.commit()

    def deletar(self,id):
        comando_sql = f"DELETE FROM BACKEND WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        

    

