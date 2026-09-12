## Exercícios
Exercícios: OOP
Exercícios — Programação Orientada a Objetos (OOP)
Coloque em prática o que você aprendeu sobre classes e objetos nesta aula.

Exercício 1 — Classe Retângulo
Crie uma classe Retangulo com atributos largura e altura. Adicione métodos calcular_area() e calcular_perimetro(). Crie dois objetos, calcule e exiba a área e o perímetro de cada um.

Exercício 2 — Classe Conta Bancária
Crie uma classe ContaBancaria com atributos titular (público) e _saldo (protegido). Implemente métodos: depositar(valor), sacar(valor) e exibir_saldo(). O saque só deve ser permitido se houver saldo suficiente. Crie uma conta, faça operações de depósito e saque, e exiba o saldo final.

Exercício 3 — Herança — Funcionários
Crie uma classe Funcionario com nome e salario_base. Crie uma classe Vendedor que herde de Funcionario e adicione o atributo comissao. Implemente um método calcular_salario_total() que retorne salario_base + comissao. Crie um funcionário comum e um vendedor, e exiba os dados de ambos.

Exercício 4 — Classe Produto com desconto
Crie uma classe Produto com nome, preco e _estoque. Adicione métodos: aplicar_desconto(porcentagem) que reduz o preço, vender(quantidade) que diminui o estoque (se houver quantidade suficiente) e exibir_dados() que mostra nome, preço atual e estoque. Teste criando um produto, aplicando desconto, vendendo e exibindo os dados.

Exercício 5 — Agenda de contatos
Crie uma classe Contato com nome, telefone e email. Crie uma classe Agenda que tenha uma lista de contatos e métodos: adicionar(contato), remover(nome), buscar(nome) e listar_todos(). Implemente um menu interativo (while True) que permita ao usuário gerenciar a agenda.

Exercício 6 — __str__ na prática
Crie uma classe Livro com atributos titulo, autor e ano. Implemente o método __str__ para que print(livro) exiba algo como "Dom Casmurro, de Machado de Assis (1899)". Crie dois livros e imprima com print().

Exercício 7 — Atributo de classe (contador)
Crie uma classe Usuario com atributos nome e email. Adicione um atributo de classe total_usuarios que conta quantos usuários foram criados. Toda vez que um novo Usuario for instanciado, o contador deve incrementar automaticamente. Crie alguns usuários e imprima o total usando Usuario.total_usuarios.

Exercício 8 — @staticmethod e @classmethod
Crie uma classe ConversorTemperatura com:

 
@staticmethod celsius_para_fahrenheit(celsius) — converte e retorna o valor em Fahrenheit
 
@staticmethod fahrenheit_para_celsius(fahrenheit) — converte e retorna o valor em Celsius
 
@classmethod descongelar_agua(cls) — retorna uma temperatura de 0°C em Fahrenheit (use o static method)
 
@classmethod ferver_agua(cls) — retorna uma temperatura de 100°C em Fahrenheit (use o static method)
Teste todos os métodos sem instanciar a classe.

Exercício 9 — Polimorfismo com formas geométricas
Crie uma classe FormaGeometrica com método area() que retorna 0. Crie as subclasses:

 
Circulo — recebe raio no construtor. area() retorna 3.14 * raio ** 2.
 
Retangulo — recebe largura e altura. area() retorna largura * altura.
 
Triangulo — recebe base e altura. area() retorna (base * altura) / 2.
Crie uma lista com uma instância de cada forma e itere com for imprimindo a área de cada uma — sem usar if para verificar o tipo.

Exercício 10 — Type hints em classes
Retome a classe ContaBancaria do Exercício 2 e reescreva-a adicionando type hints em todos os parâmetros, atributos e retornos de métodos. Depois, crie uma nova classe Banco com:

 
Atributo de classe contas: list[ContaBancaria] = []
 
@classmethod abrir_conta(cls, titular: str, saldo_inicial: float) -> ContaBancaria — cria uma conta, adiciona na lista e retorna
 
@classmethod total_contas(cls) -> int — retorna a quantidade de contas
Use type hints em TODOS os métodos e parâmetros. Teste abrindo contas e consultando o total.


ero ao Avançado com FastAPI
Resolução
Resolução: OOP
Resolução — Programação Orientada a Objetos (OOP)
Confira as soluções comentadas dos exercícios desta aula.

Exercício 1 — Classe Retângulo
Estratégia: definir os atributos no __init__ e calcular área e perímetro em métodos separados mantém cada responsabilidade isolada. Isso facilita reutilizar a classe sem precisar repetir as fórmulas no código principal.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

ret1 = Retangulo(10, 5)
ret2 = Retangulo(7, 3)

print(f"Retângulo 1 — Área: {ret1.calcular_area()}, Perímetro: {ret1.calcular_perimetro()}")
print(f"Retângulo 2 — Área: {ret2.calcular_area()}, Perímetro: {ret2.calcular_perimetro()}")
Exercício 2 — Classe Conta Bancária
Estratégia: usar _saldo com underscore sinaliza que o atributo é protegido e não deve ser alterado diretamente de fora da classe. Toda modificação passa pelos métodos depositar e sacar, que aplicam as regras de negócio antes de alterar o saldo.

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self._saldo = saldo_inicial  # underscore indica atributo protegido

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado.")
        else:
            print("Valor inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
        elif valor > self._saldo:
            print("Saldo insuficiente.")
        else:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")

    def exibir_saldo(self):
        print(f"Saldo de {self.titular}: R$ {self._saldo:.2f}")

conta = ContaBancaria("Ana", 1000.0)
conta.exibir_saldo()
conta.depositar(500)
conta.sacar(200)
conta.sacar(2000)  # deve ser bloqueado por saldo insuficiente
conta.exibir_saldo()
Exercício 3 — Herança — Funcionários
Estratégia: usar super().__init__() no construtor da classe filha evita repetir o código de inicialização da classe pai. O Vendedor sobrescreve exibir_dados() para mostrar o salário total em vez do salário base, mantendo a mesma interface de uso.

class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def exibir_dados(self):
        print(f"{self.nome} — R$ {self.salario_base:.2f}")

class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, comissao):
        super().__init__(nome, salario_base)  # delega inicialização ao pai
        self.comissao = comissao

    def calcular_salario_total(self):
        return self.salario_base + self.comissao

    def exibir_dados(self):
        total = self.calcular_salario_total()
        print(f"{self.nome} (Vendedor) — R$ {total:.2f}")  # sobrescreve para mostrar total

func = Funcionario("Bruno", 3000.0)
vend = Vendedor("Carla", 2500.0, 800.0)

func.exibir_dados()
vend.exibir_dados()
Exercício 4 — Classe Produto com desconto
Estratégia: o método aplicar_desconto modifica self.preco diretamente no objeto, acumulando descontos se chamado mais de uma vez. O atributo _estoque é protegido para que vendas só ocorram pelo método vender, onde a validação de quantidade é garantida.

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self._estoque = estoque  # protegido: só reduz pelo método vender

    def aplicar_desconto(self, porcentagem):
        if 0 < porcentagem <= 100:
            self.preco -= self.preco * (porcentagem / 100)  # altera preco no próprio objeto
            print(f"Desconto de {porcentagem}% aplicado.")
        else:
            print("Porcentagem inválida.")

    def vender(self, quantidade):
        if quantidade <= 0:
            print("Quantidade inválida.")
        elif quantidade > self._estoque:
            print("Estoque insuficiente.")
        else:
            self._estoque -= quantidade
            print(f"Venda de {quantidade} unidade(s) realizada.")

    def exibir_dados(self):
        print(f"{self.nome} — R$ {self.preco:.2f} — Estoque: {self._estoque}")

produto = Produto("Notebook", 3500.0, 10)
produto.exibir_dados()
produto.aplicar_desconto(10)
produto.vender(3)
produto.exibir_dados()
Exercício 5 — Agenda de contatos
Estratégia: separar os dados em uma classe Contato e a lógica de gerenciamento em Agenda aplica o princípio de responsabilidade única. O método remover usa return após encontrar o contato para sair do loop imediatamente, evitando continuar iterando desnecessariamente.

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar(self, contato):
        self.contatos.append(contato)
        print(f"Contato '{contato.nome}' adicionado.")

    def remover(self, nome):
        for c in self.contatos:
            if c.nome == nome:
                self.contatos.remove(c)
                print(f"Contato '{nome}' removido.")
                return  # encerra o loop ao encontrar o primeiro match
        print(f"Contato '{nome}' não encontrado.")

    def buscar(self, nome):
        for c in self.contatos:
            if c.nome == nome:
                print(f"{c.nome} — {c.telefone} — {c.email}")
                return
        print(f"Contato '{nome}' não encontrado.")

    def listar_todos(self):
        if not self.contatos:
            print("Agenda vazia.")
            return
        for c in self.contatos:
            print(f"{c.nome} — {c.telefone} — {c.email}")

agenda = Agenda()

while True:
    print("\n1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Listar todos")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "0":
        print("Saindo...")
        break
    elif opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        agenda.adicionar(Contato(nome, telefone, email))
    elif opcao == "2":
        nome = input("Nome para remover: ")
        agenda.remover(nome)
    elif opcao == "3":
        nome = input("Nome para buscar: ")
        agenda.buscar(nome)
    elif opcao == "4":
        agenda.listar_todos()
    else:
        print("Opção inválida.")
Exercício 6 — __str__ na prática
Estratégia: __str__ retorna uma string amigável para o usuário final. É o método que o Python chama automaticamente quando você usa print() ou str() em um objeto. Implementar __str__ torna seus objetos legíveis e úteis para exibição.

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f"{self.titulo}, de {self.autor} ({self.ano})"

livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("1984", "George Orwell", 1949)

print(livro1)  # Dom Casmurro, de Machado de Assis (1899)
print(livro2)  # 1984, de George Orwell (1949)
Exercício 7 — Atributo de classe (contador)
Estratégia: o atributo de classe total_usuarios é definido fora do __init__ e incrementado dentro dele com Usuario.total_usuarios += 1. Isso garante que o contador seja compartilhado entre todas as instâncias e reflita o número real de objetos criados.

class Usuario:
    total_usuarios = 0  # atributo de classe

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        Usuario.total_usuarios += 1  # incrementa o contador da classe

u1 = Usuario("Ana", "ana@email.com")
u2 = Usuario("Bruno", "bruno@email.com")
u3 = Usuario("Carla", "carla@email.com")

print(f"Total de usuários: {Usuario.total_usuarios}")  # Total de usuários: 3
Exercício 8 — @staticmethod e @classmethod
Estratégia: @staticmethod é usado para funções utilitárias que não dependem de instância nem de classe — como fórmulas de conversão. @classmethod recebe cls e pode chamar outros métodos da classe, permitindo compor comportamentos reutilizáveis.

class ConversorTemperatura:
    @staticmethod
    def celsius_para_fahrenheit(celsius):
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_para_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @classmethod
    def descongelar_agua(cls):
        return cls.celsius_para_fahrenheit(0)

    @classmethod
    def ferver_agua(cls):
        return cls.celsius_para_fahrenheit(100)

print(ConversorTemperatura.celsius_para_fahrenheit(25))  # 77.0
print(ConversorTemperatura.fahrenheit_para_celsius(77))  # 25.0
print(ConversorTemperatura.descongelar_agua())           # 32.0
print(ConversorTemperatura.ferver_agua())                # 212.0
Exercício 9 — Polimorfismo com formas geométricas
Estratégia: cada subclasse sobrescreve area() com sua própria fórmula. O loop itera uma lista heterogênea e chama forma.area() sem se preocupar com o tipo — cada objeto responde com seu próprio cálculo. Isso é polimorfismo em ação.

class FormaGeometrica:
    def area(self):
        return 0

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Triangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

formas = [
    Circulo(5),
    Retangulo(4, 6),
    Triangulo(3, 8),
]

for forma in formas:
    print(f"Área: {forma.area():.2f}")
# Área: 78.50
# Área: 24.00
# Área: 12.00
Exercício 10 — Type hints em classes
Estratégia: type hints são adicionados nos parâmetros (nome: str), retornos (-> None) e atributos (self.atributo: tipo = valor). O @classmethod abrir_conta age como factory, e total_contas consulta o estado da classe sem precisar de instância.

class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0.0) -> None:
        self.titular: str = titular
        self._saldo: float = saldo_inicial

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado.")
        else:
            print("Valor inválido.")

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            print("Valor inválido.")
        elif valor > self._saldo:
            print("Saldo insuficiente.")
        else:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")

    def exibir_saldo(self) -> None:
        print(f"Saldo de {self.titular}: R$ {self._saldo:.2f}")

class Banco:
    contas: list = []  # type hint no atributo de classe

    @classmethod
    def abrir_conta(cls, titular: str, saldo_inicial: float) -> ContaBancaria:
        conta = ContaBancaria(titular, saldo_inicial)
        cls.contas.append(conta)
        return conta

    @classmethod
    def total_contas(cls) -> int:
        return len(cls.contas)

c1 = Banco.abrir_conta("Ana", 1000.0)
c2 = Banco.abrir_conta("Bruno", 500.0)

c1.exibir_saldo()
print(f"Total de contas no banco: {Banco.total_contas()}")  # 2