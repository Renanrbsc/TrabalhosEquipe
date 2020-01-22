from Model.frontend import FrontEnd
from Model.backend import BackEnd

class Squads:
    
    def __init__(self):   
        self.id = 0
        self.name_squad = ''
        self.descricao = ''
        self.numero_pessoas = 0
        self.linguagembackend = BackEnd()
        self.linguagemfrontend = FrontEnd()
    
    def __str__(self):
        return f'{self.id};{self.name_squad};{self.descricao};{self.numero_pessoas};{self.linguagembackend};{self.linguagemfrontend}'



    print('ola')