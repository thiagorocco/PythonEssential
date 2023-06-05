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
        self.frame_cima = Frame(self.janela_principal)
        self.frame_baixo = Frame(self.janela_principal)

        #Criando os labels
        
        self.label1 = Label(self.frame_cima, text='To no frame de cima!')
        self.label2 = Label(self.frame_baixo, text='To no frame de baixo!')

        #Posicionando os labels nos frames
        self.label1.pack(side='top')
        self.label2.pack(side='top')

        #Posicionando o frame
        self.frame_cima.pack()
        self.frame_baixo.pack()

        #Fazer o Tkinter exibir o looping da janela
        mainloop()
minha_gui = MinhaGUI()        