import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = 'Primeira Janela'

        #Chamando a janela
        self.carregarJanela()

    def carregarJanela(self):
        #setGeometry(Distância da esquerda, distância do topo, largura, altura )
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()#mostrar janela

#Criamos um objeto QApplication com o parametro sys.argv que possibilita trabalhar com
#eventos do sistema como fechar janela, entre outros
aplicacao = QApplication(sys.argv)

#Criamos um objeto da nossa classe Janela que herda a classe QMainWindow e já tem todos 
# os parametros configurados
j = Janela()
#Por fim, passamos como parametro ao método exit o método exec do objeto aplicacao,
# ele aguardará que o exec seja acionado para encerrar a aplicação, isso ocorre quando 
#o usuário clicar no "X" na janela
sys.exit(aplicacao.exec_())