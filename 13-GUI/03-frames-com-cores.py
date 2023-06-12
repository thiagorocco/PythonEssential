'''

Frame(Quadro) É uma espécie de 'container', cujo propósito principal é armazenar 
e agrupar outros widgets.

'''
from tkinter import *

class MinhaGUI:
    def __init__(self):
        #Criando a janela principal
        self.janela_principal = Tk()

        #Criando os frames
        #Ordem dos parâmetros: Janela Principal, Background(Cor), altura(heigth),largura(width)
        self.frame_cima = Frame(self.janela_principal,bg='white',height=70,width=400)
        self.frame_baixo = Frame(self.janela_principal,bg='red',height=70,width=400)

        #Posicionando o frame
        self.frame_cima.pack()#side='left' inverte a posição das cores, lado a lado
        self.frame_baixo.pack()

        #Fazer o Tkinter exibir o looping da janela
        mainloop()
minha_gui = MinhaGUI()        