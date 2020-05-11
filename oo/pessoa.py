# PEP 8
# toda classe deve comçar com letra maiuscula, se houver outra palavra, CamelCase

class Pessoa:
    
    ##
    def cumprimentar(self):
        return f'Olá {id(self)}'
    
    
if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    