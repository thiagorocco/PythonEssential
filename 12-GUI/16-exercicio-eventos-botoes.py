from email import message
from tkinter import *
from tkinter import messagebox

#Herdando a classe Frame
class EventosBottoes(Frame):
    def __init__(self):
        #inicializando o construtor da classe Frame
        Frame.__init__(self)
        self.pack()
        self.master.title('Botões')
        self.master.geometry('240x80')

        #Criando os botões
        self.botao1 = Button(self, text='FLAT',command=self.apertou)
        self.botao2 = Button(self, text='GROOVE',command=self.apertou)
        self.botao3 = Button(self, text='RIDGE',command=self.apertou)
        self.botao4 = Button(self, text='SUNKEN',command=self.apertou)

        #Vinculando eventos aos botões
        self.botao1.bind('<Enter>',self.passou_por_cima1)
        self.botao1.bind('<Leave>',self.saiu_de_cima)
        self.botao2.bind('<Enter>',self.passou_por_cima2)
        self.botao2.bind('<Leave>',self.saiu_de_cima)
        self.botao3.bind('<Enter>',self.passou_por_cima3)
        self.botao3.bind('<Leave>',self.saiu_de_cima)
        self.botao4.bind('<Enter>',self.passou_por_cima4)
        self.botao4.bind('<Leave>',self.saiu_de_cima)

        #Empacotando os botões
        self.botao1.pack(side='left')
        self.botao2.pack(side='left')
        self.botao3.pack(side='left')
        self.botao4.pack(side='left')

        #Rodando
        mainloop()
    def apertou(self):
        messagebox.showinfo('Mensagem','Apertou o botão')
    def passou_por_cima1(self,event):
        event.widget.config(relief = FLAT)
    def passou_por_cima2(self,event):
        event.widget.config(relief = GROOVE)
    def passou_por_cima3(self,event):
        event.widget.config(relief = RIDGE)
    def passou_por_cima4(self,event):
        event.widget.config(relief = SUNKEN)
    def saiu_de_cima(self, event):
        event.widget.config(relief = RAISED)

EventosBottoes()