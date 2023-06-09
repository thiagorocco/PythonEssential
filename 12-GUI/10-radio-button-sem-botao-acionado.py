from tkinter import *
from tkinter import messagebox
'''
Aqui em vez de atribuir o comando com a função exibe para um botão 
vamos atribuí-lo ao próprio radio button. Assim que for manipulado
exibirá o valor
'''
class MinhaGUI:
 def __init__(self):
  # Cria janela principal
  self.janela_principal = Tk()
  
  # Criando o frame
  self.frame_cima = Frame(self.janela_principal)
  
  # Objeto IntVar dos botões
  self.radio_valor = IntVar()
  self.radio_valor.set(1)  # Para a primeira opção ficar marcada
  
  # Criando os radio buttons e o label
  self.label = Label(self.frame_cima, text='Qual o melhor curso?')
  self.python = Radiobutton(self.frame_cima, text='Python Progressivo', \
       variable = self.radio_valor, value=1, command=self.exibe)
  self.java = Radiobutton(self.frame_cima, text='Java Progressivo', \
       variable = self.radio_valor, value=2, command=self.exibe)
  self.c = Radiobutton(self.frame_cima, text='C Progressivo', \
       variable = self.radio_valor, value=3, command=self.exibe)
  
  # Empacotando o label e os radio buttons
  self.label.pack(anchor = 'w')
  self.python.pack(anchor = 'w')
  self.java.pack(anchor = 'w')
  self.c.pack(anchor = 'w')
  
  
  # Empacotando o frame na janela principal
  self.frame_cima.pack()
  
  # Rodando
  mainloop()
  
 def exibe(self):
   nome = str(self.radio_valor.get())
   messagebox.showinfo('Resposta','Você escolheu a opçao ' + nome)
   
  
gui = MinhaGUI()