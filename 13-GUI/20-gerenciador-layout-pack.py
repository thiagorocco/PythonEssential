'''
    Gerenciador de Layout Pack
    Por padrão, ele vai adicionando os widgets na ordem quem forem empacotados 
    (chamando o método pack() ), de cima pra baixo.

    Porém, existem várias opções para empacotar os componentes:

    # side - indica de que lado você quer que seja adicionado (TOP, BOTTOM, LEFT e RIGHT). 
        Se quer um alinhamento horizontal, use side=LEFT, por exemplo
    # fill - para preencher um espaço. Pode usar como argumneto X, Y ou BOTH, 
        e ele vai cobrir todo o espaçamento horizontal (X), vertical (Y) ou ambos (BOTH)
    # expand - pode passar como YES ou NO, para definir se o widget vai preencher todo 
        o espaço extra do container ou não.
    # padx e pady - preenchem o ao redor do widget com espaço em branco
    # pack_forget - retira um widget empacotado do container que foi inserido anteriormente

'''
from tkinter import *
class PackDemo(Frame):
    def __init__(self):
        #Inicializando o Frame
        Frame.__init__(self)
        self.master.title('Gerenciador de Pack')
        self.master.geometry('600x250')
        self.pack(expand=YES, fill=BOTH)

        #Botão que adiciona outros, no topo
        self.botao1 = Button(self,text='Adicionar Botão',command=self.adicionarBotao)
        self.botao1.pack(side=TOP)

        #Botão 2, no fundo e preeche X e Y
        self.botao2 = Button(self,text='expand = NO fill = BOTH')
        self.botao2.pack(side=BOTTOM, fill = BOTH)
        
        # Botão3: na esquerda, fill só na horizontal
        self.botao3 = Button( self, text = "expand = YES, fill = X" )
        self.botao3.pack( side = LEFT, expand = YES, fill = X )

        # Botão4: na direita, fill só na vertical
        self.botao4 = Button( self, text = "expand = YES, fill = Y" )
        self.botao4.pack( side = RIGHT, expand = YES, fill = Y )

        mainloop()
    def adicionarBotao(self):
        Button(self,text='Botão Novo').pack(pady = 5)
PackDemo() 