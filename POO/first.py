#criando a classe
class Computador:
    #construtor -> Funcionalidade inicial da classe
    def __init__(self, marca = 'Samsung', memoriaRam = '16gb', armazenamento = '120gb'):
        #self serve pra acessar as propriedades e métodos de uma instância, além de que tudo que está com self poder ser acessado em qualquer local da classe
        self.marca = marca
        self.memoriaRam = memoriaRam
        self.armazenamento = armazenamento

    def ligar(self):
        print('Ligando')

    def desligar(self):
        print('Desligando')

    def exibirInfo(self):
        print(self.marca, self.memoriaRam, self.armazenamento)

#instanciando um objeto pra representar a classe
#cada instancia/variável é diferente uma da outra, suas propriedades serão diferentes umas das outras
computador1 = Computador('Lenovo','8gb','500gb')
computador1.marca = 'Lenovo'
computador1.memoriaRam = '128gb'
computador1.armazenamento = '500gb'

print(computador1.exibirInfo())

computador2 = Computador()
print(computador2.ligar())
print(computador2.exibirInfo())