'''
    Dizemos que a programação gráfica é event driven, 
    ou seja, acionada por eventos.
    
    Os programas em GUI são ditos assíncronos, 
    pois eles rodam e ficam lá parados, esperando o usuário fazer algo

    o evento handler nada mais é que um bom e velho conhecido método que
     é sempre invocado quando um evento ocorre.

    <Button-1> se refere ao botão mais a esquerda do mouse.
    <Button-2> se refere ao botão do meio, quando existe.
    <Button-3> é o evento que se refere ao botão mais a direita.

    O Python fica na espreita, aguardando algum evento ocorrer. 
    Se ocorrer, ele identifica qual foi e chama o handler correspondente.
'''
from tkinter import *

#É o event handler
def tratador_evento(event):
    print('Você clicou  na posição:',event.x,event.y)

janela_principal = Tk()
meuFrame = Frame(janela_principal,width=500,height=500)
meuFrame.bind('<Button-1>',tratador_evento)
meuFrame.pack()

mainloop()