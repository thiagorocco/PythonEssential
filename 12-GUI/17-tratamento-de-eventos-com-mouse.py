'''
    Vamos usar 5 eventos:
    <Button-1> - Botão 1 do mouse (mais a esquerda) é pressionado
    <ButtonRelease-1> - Botão 1 é liberado (released)
    <Enter> - Mouse entrou no frame (janela)
    <Leave> - Mouse deixou o frame da janela
    <B1-Motion> - Botão 1 do mouse foi arrastado (clicar e segurar) 
'''
from tkinter import *

class MouseEvent(Frame):
    def __init__(self):
        #Criando o frame, título e tamanho
        Frame.__init__(self)
        self.pack(expand = YES, fill = BOTH)
        self.master.title('Eventos com mouse')
        self.master.geometry('300x200')

        #String com a posição do mouse
        self.mousePosicao = StringVar()
        self.mousePosicao.set('Mouse fora da janela')

        #Criando e posicionando o label embaixo
        self.positionLabel = Label(self, textvariable=self.mousePosicao)
        self.positionLabel.pack(side=BOTTOM)

        #Criando os binds com os eventos de mouse
        self.bind('<Button-1>',self.botaoPressionado)
        self.bind('<ButtonRelease-1>',self.botaoLiberado)
        self.bind('<Enter>',self.entrouJanela)
        self.bind('<Leave>',self.saiuJanela)
        self.bind('<B1-Motion>',self.mouseArrastado)

        mainloop()
    def botaoPressionado(self, event):
        self.mousePosicao.set('Pressionado em ['+str(event.x)+','+str(event.y)+']')
    def botaoLiberado(self, event):
        self.mousePosicao.set('Solto em ['+str(event.x)+','+str(event.y)+']')
    def entrouJanela(self, event):
        self.mousePosicao.set('Mouse na Janela')
    def saiuJanela(self, event):
        self.mousePosicao.set('Mouse fora da Janela')
    def mouseArrastado(self, event):
        self.mousePosicao.set('Arrastado até ['+str(event.x)+','+str(event.y)+']')

MouseEvent()