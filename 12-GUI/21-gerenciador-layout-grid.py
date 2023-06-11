'''
    Vai dividir o container em uma grade (grid em inglês), 
    assim podemos posicionar os elementos dividindo o Frame, 
    por exemplo, em x linhas e y linhas.

    Cada posição é chamada de célula, ou seja, cada célular é composta por 
    um valor de linha, um valor de coluna e pode ter um widget

    A primeira linha (row) é a 0, a segunda coluna é a de número 1, a terceira é de número 2...
    A primeira coluna (column) é a 0, a segunda é a 1, a terceira é a 2...

    Sempre que quiser dispor seus elementos, alinhados por linhas e colunas, use o grid.
'''
from tkinter import *

class Grid(Frame):
    def __init__(self):
        #Inicializando o frame
        Frame.__init__(self)
        self.master.title('Grid')
        self.master.geometry('80x80')

        #Criando os labels e adicionando
        #com o método grid
        for linha in range(3):
            for coluna in range(3):
                Label(self.master, text=str(linha)+','+str(coluna)).grid(row=linha,column=coluna)
        mainloop()
class Grid2(Frame):
    def __init__(self):
        # Inicializando o frame 
        Frame.__init__(self)
        self.master.title("Grid")
        
        Label(self.master, text="Nome").grid(row=0)
        Label(self.master, text="Sobrenome").grid(row=1)

        entrada1 = Entry(self.master)
        entrada2 = Entry(self.master)

        entrada1.grid(row=0, column=1)
        entrada2.grid(row=1, column=1)

        mainloop()
Grid()
Grid2()


