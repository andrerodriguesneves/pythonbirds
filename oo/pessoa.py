# PEP 8
# toda classe deve comçar com letra maiuscula, se houver outra palavra, CamelCase

class Pessoa:
    
    # atributos de classe 
    # pode ser acessado direto pela classe exmplo: Pessoa.olhos
    olhos = 2 
    
    # atributos de instancia
    def __init__(self, *filhos,  nome=None, idade=35):
        self.nome = nome
        self.idade = idade 
        self.filhos = list(filhos)
        
    
    ##
    def cumprimentar(self):
        return f'Olá {id(self)}'
    
    
    @staticmethod
    def metodo_estatico():
        print('Ola Mundo')
    
if __name__ == '__main__':
    andre = Pessoa(nome='André')
    luiz = Pessoa(andre, nome='Luiz')
   
    print(Pessoa.cumprimentar(luiz))
    print(id(luiz))
    print(luiz.cumprimentar())
    print(luiz.nome)
    print(luiz.idade)
    for filhos in luiz.filhos:
        print(filhos.nome)

    # atributo dinamico | __dict__        
    luiz.sobrenome = 'Neves'
    luiz.olhos = 1 
    Pessoa.olhos = 3
    print(luiz.sobrenome)
    print(luiz.__dict__)
    print(andre.__dict__)
    print(Pessoa.olhos)
    print(andre.olhos)
    print(luiz.olhos)

    Pessoa.metodo_estatico()
    
    luiz.metodo_estatico()
