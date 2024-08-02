class Animal:
    nome = str
    cor = str
    idade = int
    peso = float
    raca = str
    def __init__(self,nome,cor,idade,peso,raca) :
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.peso= peso
        self.raca = raca

class Humano (Animal):
     
    religiao = str
    rg = str
    profissao = str

    def __init__(self,nome,cor,idade,peso,raca,rg,profissao,religiao):
        super().__init__(nome,cor,idade,peso,raca)
        self.religiao = religiao
        self.rg = rg
        self.profissão = profissao


class Cachorro (Animal):

    porte = str
    dono = str

    def __init__(self,nome,cor,idade,peso,raca,porte,dono) :
        super().__init__(nome,cor,idade,peso,raca)
        self.porte = porte
        self.dono = dono

    def latir(self):
        print("AU-AU")

# def criar_cao():
#         Nome = input("Digite um nome: ")
#         Cor = input("Digite a Cor: ")
#         idade = int(input("Digite o Idade: "))
#         Peso = int(input("Qual o peso: "))
#         Raça = input("Qual a raça: ")
#         Porte = input("Digite o porte: ")
#         dono = input("nome do dono: ")
#         cao = Cachorro(Nome,Cor,idade,Peso,Raça,Porte,dono)
#         return cao

# criar_cao()













    # def adicionar_pessoa ():
    #     nome = input("Digite um nome: ")
    #     idade = input("Digite a idade: ")
    #     raça = input("Qual a raça: ")
    #     pessoa = Humano(nome,idade,raça)