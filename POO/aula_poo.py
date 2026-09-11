# programacao orientada a objetos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.") 
        
        
pessoa1 = Pessoa("Alice", 30)
pessoa1.apresentar()  # Olá, meu nome é Alice e eu tenho 30 anos.
pessoa2 = Pessoa("Bob", 25)
pessoa2.apresentar()  # Olá, meu nome é Bob e eu tenho 25 anos.