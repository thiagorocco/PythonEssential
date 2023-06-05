from tkinter import *

class MinhaGUI:
    def __init__(self):
        #Criando 2 janelas
        self.janela1 = Tk()
        self.janela2 = Tk()

        #Bandeira da França
        self.frame1 = Frame(self.janela1, bg='blue',height=200, width=80)
        self.frame2 = Frame(self.janela1, bg='white',height=200, width=80)
        self.frame3 = Frame(self.janela1, bg='red',height=200, width=80)
        self.frame1.pack(side='left')
        self.frame2.pack(side='left')
        self.frame3.pack(side='left')

        #Bandeira da Holanda
        self.quadro1 = Frame(self.janela2, bg='red',height=80,width=200)
        self.quadro2 = Frame(self.janela2, bg='white',height=80,width=200)
        self.quadro3 = Frame(self.janela2, bg='blue',height=80,width=200)
        self.quadro1.pack(side='top')
        self.quadro2.pack(side='top')
        self.quadro3.pack(side='top')

        #Fazer o tkinter exibir as janelas em looping
        mainloop()

minha_gui = MinhaGUI()