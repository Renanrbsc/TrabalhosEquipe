import MySQLdb
from Model.squads import Squads 

class SquadsDao:
    conexao = MySQLdb.connect(host = '127.0.0.1',
                              database = 'PadawanHBSIS',
                              user = 'root')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando_sql = f"SELECT * FROM SQUADS_DEV"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
        
    def listar_por_id(self,id):
        comando_sql = f"SELECT * FROM SQUADS_DEV WHERE CODIGO = {id}"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squads:Squads):
        comando_sql = f"""INSERT INTO SQUADS_DEV
        (
            NAME_SQUAD,
            DESCRICAO,
            NUMERO_PESSOAS,
            LINGUAGEMBACKEND,
            LINGUAGEMFRONTEND
        )
        VALUES
        (
            '{squads.name_squad}',
            '{squads.descricao}',
             {squads.numero_pessoas},
            '{squads.linguagembackend}',
            '{squads.linguagemfrontend}'
        )"""
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, squads:Squads, id):
        comando_sql = f"""UPDATE SQUADS_DEV
        SET 
            NAME_SQUAD = '{squads.name_squad}',
            DESCRICAO = '{squads.descricao}',
            NUMERO_PESSOAS = {squads.numero_pessoas},
            LINGUAGEMBACKEND = '{squads.linguagembackend}',
            LINGUAGEMFRONTEND = '{squads.linguagemfrontend}'
        WHERE CODIGO = {id}
        """
        self.cursor.execute(comando_sql)
        self.conexao.commit()

    def deletar(self,id):
        comando_sql = f"DELETE FROM SQUADS_DEV WHERE CODIGO = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        

    

