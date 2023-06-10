'''
    Vamos usar dois eventos:
    <Enter> : Quando você passa o mouse por cima do botão
    <Leave>: Quando você tira o mouse de cima do botão

    Esses métodos de tratamento de evento vão simplesmente mudar a textura do botão.
    Quando passa o mouse por cima, temos o estilo GROOVE (de entrar, simulando o botão entrando.
    Quando tiramos o mouse de cima, acionamos o estilo RAISED (de levantar o botão que estava
    para dentro).

    E quando apertamos o botão, o método apertou é acionado.
'''
from tkinter import *
from tkinter import messagebox

class ButtonEvent(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.master.title('Botão')
        self.master.geometry('120x40')

        #Criando o botão
        self.botao = Button(self,text = 'Clique aqui',command= self.apertou)
        self.botao.bind('<Enter>',self.passou_por_cima)
        self.botao.bind('<Leave>',self.saiu_de_cima)
        self.botao.pack(side = LEFT, padx = 5, pady = 5)

        mainloop()
    def apertou(self):
        messagebox.showinfo('Mensagem','Você apertou o botão')
    def passou_por_cima(self,event):
        event.widget.config(relief = GROOVE)
    def saiu_de_cima(self, event):
        event.widget.config(relief = RAISED)
ButtonEvent()    
