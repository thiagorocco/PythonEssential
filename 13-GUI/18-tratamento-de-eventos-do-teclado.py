'''
    <KeyPress> ou <Key> - Dispara quando qualquer tecla é pressionada
    <KeyRelease> - Dispara quando uma tecla é solta ou liberada
    <KeyPress-tecla> ou <Key-tecla> - Quando uma tecla específica, a tecla, é pressionada
    <KeyRelease-tecla> - Quando a tecla específica é solta ou liberada
    <key> - Abreviação ou atalho, faz o mesmo de <KeyPress-tecla>
    <prefixo-tecla> - Dispara quando você aperta a tecla específica tecla enquanto 
    segura a prefixo. Esse prefixo pode ser Alt, Shift ou Control apenas.
'''
from tkinter import *

class KeyboardEvent(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Eventos de teclado")
        self.master.geometry("250x50")

        # Label e Stringvar que vao exibir a tecla
        self.mensagem = StringVar()
        self.label = Label(self, textvariable = self.mensagem)
        self.mensagem.set("Aperte uma tecla" )
        self.label.pack()
        
        # Fazendo os binding no frame
        self.master.bind( "<KeyPress>", self.teclaPressionada )
        self.master.bind( "<KeyRelease>", self.teclaLiberada )
        self.master.bind( "<KeyPress-Alt_L>", self.altPressionado )
        self.master.bind( "<KeyRelease-Alt_L>", self.altLiberado )
        
        mainloop()

    def teclaPressionada( self, event ):
        self.mensagem.set( "Tecla pressionada: " + event.char )
    def teclaLiberada( self, event ):
        self.mensagem.set( "Tecla solta: " + event.char )
    def altPressionado( self, event ):
        self.mensagem.set( "Alt pressionado" )
    def altLiberado( self, event ):
        self.mensagem.set( "Alt liberado")

KeyboardEvent()