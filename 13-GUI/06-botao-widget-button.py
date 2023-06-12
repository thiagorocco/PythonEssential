'''
    Para criarmos um botão, usamos a classe Button, que recebe três parâmetros:

    1. A janela mestre (objeto do tipo Tk() )
    2. text: string com o texto que vai aparecer no botão (Ok, Cancelar, Sair...)
    3. command: nome do método ou função que vai ser chamado quando clicarmos no botão.
'''
from tkinter import *
from tkinter import messagebox

class MinhaGUI:
    def __init__(self):
        #Criamos a janela principal
        self.janela_principal = Tk()

        #Criando o botão
        self.botao = Button(self.janela_principal,text='Clique aqui',command=self.hello_world)
        self.botao_sair = Button(self.janela_principal,text='Sair',command=self.janela_principal.quit)

        #Empacotando o botão na janela principal
        self.botao.pack()
        self.botao_sair.pack()

        #Rodando
        mainloop()
    
    def hello_world(self):
        messagebox.showinfo('Saudações','Hello, World!')

minha_gui = MinhaGUI()