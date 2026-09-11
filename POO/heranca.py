class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass
    
class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"
    
    
class Professor:
    def __init__(self,nome,identificacao_registro):
        self.nome = nome
        self.identificacao_registro = identificacao_registro
        
class Docente_Tecnico(Professor):
    def __init__(self,nome,identificacao_registro,area_atuacao):
        super().__init__(nome,identificacao_registro)
        self.area_atuacao = area_atuacao
        
class Docente_AnosFinais(Professor):
    def __init__(self,nome,identificacao_registro,disciplina):
        super().__init__(nome,identificacao_registro)
        self.disciplina = disciplina