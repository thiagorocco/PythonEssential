from tkinter import *
from tkinter import messagebox

class EntryTeste( Frame ):
    def __init__( self ):
        # Inicializando os frames, títulos e tamanhos
        Frame.__init__( self )
        self.pack( expand = YES, fill = BOTH )
        self.master.title( "Componentes de entrada" )
        self.master.geometry( "325x100" ) # width x length
  
        # Criando o primeiro frame que vai armazenar
        # as duas primeiras caixas de entrada
        self.frame1 = Frame( self )
        self.frame1.pack( pady = 5 )
        
        # Criando a primeira caixa de entrada
        self.text1 = Entry( self.frame1, name = "caixa1" )
  
        # Associando o evento <Return> com o
        # event handler exibe()
        self.text1.bind( "<Return>", self.exibe )
        self.text1.pack( side = LEFT, padx = 5 )
        
        # Criando a segunda caixa e seu bind
        self.text2 = Entry( self.frame1, name = "caixa2" )
        self.text2.insert( INSERT, "Digite um texto aqui" )
        self.text2.bind( "<Return>", self.exibe )
        self.text2.pack( side = LEFT, padx = 5 )
        
        # Segundo frame, com as duas outras caixas
        self.frame2 = Frame( self )
        self.frame2.pack( pady = 5 )
  
        # Criando a caixa que não dá pra editar
        self.text3 = Entry( self.frame2, name = "caixa3" )
        self.text3.insert( INSERT, "Texto ineditável" )
        self.text3.config( state = DISABLED )
        self.text3.bind( "<Return>", self.exibe )
        self.text3.pack( side = LEFT, padx = 5 )
        
        # Criando a caixa estilo senha
        self.text4 = Entry( self.frame2, name = "caixa4", show = "*" )
        self.text4.insert( INSERT, "Texto escondido" )
        self.text4.bind( "<Return>", self.exibe )
        self.text4.pack( side = LEFT, padx = 5 )
  
        mainloop()
 
    def exibe( self, event ):
        # Pegando o nome do widget
        nomeCaixa = event.widget.winfo_name()
        # Pegando o conteúdo do widget
        conteudoCaixa = event.widget.get()
        messagebox.showinfo( "Texto na caixa", nomeCaixa + ": " + conteudoCaixa )
  
# Chamando a classe
EntryTeste()