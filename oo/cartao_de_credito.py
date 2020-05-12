class Cartao:
    
    
    def __init__(self, bandeira):
        self.bandeira = bandeira
        
    
    
    # decorator
    @staticmethod
    def calcula_juros_parcelas(numero_parcelas, bandeira,total_compra, juros):
        if bandeira == 'VISA':
            pass
        elif bandeira == 'MASTER':
            pass
        elif bandeira == 'AMEX':
            pass
        else:
            print('Bandeira nao cadastrda nos nossos sistemas')
            
        
    