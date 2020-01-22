import MySQLdb
from Model.squads import Squads

class SquadsDao:
    conexao = MySQLdb.connect(host = '127.0.0.1',
                              database = 'PadawanHBSIS',
                              user = 'root')
    cursor = conexao.cursor()
    
    def listar_todos(self):
        comando_sql = f"SELECT * FROM SQUAD AS S LEFT JOIN BACKEND AS B FRONTEND AS F ON S.ID_BACKEND = B.ID AND S.ID_FRONTEND = F.ID"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
        
    def listar_por_id(self,id):
        comando_sql = f"SELECT * FROM SQUAD AS S LEFT JOIN BACKEND AS B FRONTEND AS F ON S.ID_BACKEND = B.ID AND S.ID_FRONTEND = F.ID WHERE S.ID = {id}"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squads:Squads):
        comando_sql = f"""INSERT INTO SQUAD
        (
            NAME_SQUAD,
            DESCRICAO,
            NUMERO_PESSOAS,
            ID_BACKEND,
            ID_FRONTEND
        )
        VALUES
        (
            '{squads.name_squad}',
            '{squads.descricao}',
             {squads.numero_pessoas},
            {squads.linguagembackend.id},
            {squads.linguagemfrontend.id}
        )"""
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, squads:Squads):
        comando_sql = f"""UPDATE SQUAD
        SET 
            NAME_SQUAD = '{squads.name_squad}',
            DESCRICAO = '{squads.descricao}',
            NUMERO_PESSOAS = {squads.numero_pessoas},
            ID_BACKEND = {squads.linguagembackend.id},
            ID_FRONTEND = {squads.linguagemfrontend.id}
        WHERE CODIGO = {squads.id}
        """
        self.cursor.execute(comando_sql)
        self.conexao.commit()

    def deletar(self,id):
        comando_sql = f"DELETE FROM SQUAD WHERE CODIGO = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        

    

