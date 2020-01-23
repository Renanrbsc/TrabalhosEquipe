import MySQLdb
from Model.squads import Squads

class SquadsDao:
    conexao = MySQLdb.connect(host = 'mysql.padawans.dev',
                              database = 'padawans16',
                              user = 'padawans16',
                              passwd = 'lr2019')
    cursor = conexao.cursor()
    
    def listar_todos(self):
        comando_sql = f"SELECT * FROM SQUAD AS S LEFT JOIN BACKEND AS B ON S.ID_BACKEND = B.ID INNER JOIN FRONTEND AS F ON S.ID_FRONTEND = F.ID INNER JOIN SGBDS AS D ON S.ID_SGBDS = D.ID"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
        
    def listar_por_id(self,id):
        comando_sql = f"SELECT * FROM SQUAD AS S LEFT JOIN BACKEND AS B ON S.ID_BACKEND = B.ID INNER JOIN FRONTEND AS F ON S.ID_FRONTEND = F.ID INNER JOIN SGBDS AS D ON S.ID_SGBDS = D.ID WHERE S.ID = {id}"
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
            ID_FRONTEND,
            ID_SGBDS
        )
        VALUES
        (
            '{squads.name_squad}',
            '{squads.descricao}',
             {squads.numero_pessoas},
            {squads.lingbackend.id},
            {squads.lingfrontend.id},
            {squads.lingsgbds.id}
        )"""
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, squads:Squads, id):
        comando_sql = f"""UPDATE SQUAD
        SET 
            NAME_SQUAD = '{squads.name_squad}',
            DESCRICAO = '{squads.descricao}',
            NUMERO_PESSOAS = {squads.numero_pessoas},
            ID_BACKEND = {squads.lingbackend.id},
            ID_FRONTEND = {squads.lingfrontend.id},
            ID_SGBDS = {squads.lingsgbds.id}
        WHERE ID = {id}
        """
        self.cursor.execute(comando_sql)
        self.conexao.commit()

    def deletar(self,id):
        comando_sql = f"DELETE FROM SQUAD WHERE CODIGO = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        

    

