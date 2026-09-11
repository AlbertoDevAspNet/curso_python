class Carro:
    #método construtor
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0  # Velocidade inicial do carro

    def exibir_informacoes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"
    
    def acelerar(self):
        return f"O carro {self.modelo} está acelerando."
    
    def frear(self):
        return f"O carro {self.modelo} está freando. para de {self.velocidade} km/h."
    
    
    
carro1 = Carro("Toyota", "Corolla", 2020)
print(carro1.exibir_informacoes())  # Marca: Toyota, Modelo: Corolla   