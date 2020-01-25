from Model.frontend import FrontEnd
from Model.backend import BackEnd
from Model.sgbds import Sgbds

class Squads:
    
    def __init__(self):   
        self.id = 0
        self.name_squad = ''
        self.descricao = ''
        self.numero_pessoas = 0
        self.lingbackend = BackEnd()
        self.lingfrontend = FrontEnd()
        self.lingsgbds = Sgbds()
        self.id_lingbackend = 0
        self.id_lingfrontend = 0
        self.id_lingsgbds = 0
    
    def __str__(self):
        return f'{self.id};{self.name_squad};{self.descricao};{self.numero_pessoas};{self.lingbackend.id};{self.lingfrontend.id};{self.lingsgbds.id}'



    print('ola')