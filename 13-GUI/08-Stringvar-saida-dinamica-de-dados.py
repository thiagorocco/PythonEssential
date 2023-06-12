from tkinter import *

class MinhaGUI:
    def __init__(self):
        #Cria a janela principal
        self.janela_principal = Tk()

        #Cria 3 frames
        self.frame_cima = Frame(self.janela_principal)
        self.frame_meio = Frame(self.janela_principal)
        self.frame_baixo = Frame(self.janela_principal)

        #No label de cima, um label e uma entry
        self.label1 = Label(self.frame_cima,text='Digite seu nome: ')
        self.entrada = Entry(self.frame_cima, width=30)

        #Empacotando o label e entrada no primeiro frame
        self.label1.pack(side='left')
        self.entrada.pack(side='left')

        #Labels do frame do meio
        self.label2 = Label(self.frame_meio,text='Seu nome é: ')
        self.label_dinamica = StringVar()
        self.label3 = Label(self.frame_meio,textvariable=self.label_dinamica)

        #Empacotando as labels do meio
        self.label2.pack(side='left')
        self.label3.pack(side='left')
        
        #Criando os botões
        self.botao = Button(self.frame_baixo,text='Exibe',command=self.exibe)
        self.botao_sair = Button(self.frame_baixo,text='Sair', command=self.janela_principal.quit)

        #Empacotando botões e label
        self.botao.pack(side='left')
        self.botao_sair.pack(side='left')

        #Empacotando os frames na janela principal
        self.frame_cima.pack()
        self.frame_meio.pack()
        self.frame_baixo.pack()

        #Rodando
        mainloop()

    def exibe(self):
        nome = self.entrada.get()
        self.label_dinamica.set(nome)

gui = MinhaGUI()
