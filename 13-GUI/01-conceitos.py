'''
    TKinter - Tool Kit Interface, é um famoso módulo de interface gráfica para o usuário(GUI)

    O módulo Tkinter possui 15 widgets:

    1. Button: botões, onde algum evento ocorre quando clicamos
    2. Checkbutton : aqueles botões de check, tipo on e off
    3. Radiobutton: botões do tipo radio, onde é permitido escolher apenas uma opção (Masculino ou Feminino, por exemplo)
    4. Canvas: uma área retangular, que podemos colocar e exibir coisas dentro, como uma imagem
    5. Entry: um campo de entrada, onde o usuário pode digitar alguma linha de informação
    6. Frame: um 'container', uma área que serve pra abrigar e agrupar outros widgets
    7. Label: rótulo, uma área que exibe um texto ou uma imagem
    8. Listbox: uma lista de opções para o usuário marcar o que quiser
    9. Menu: uma lista de opções, um menu, onde o usuário vai clicar em alguma opção e algo vai ocorrer
    10. Menubutton: menu que é exibido na tela e pode ser clicado pelo usuário
    11. Message: mostra múltiplas linha de texto na tela
    12. Scale: um widget onde o usuário pode clicar, segurar e mover um ao longo de uma faixa (tipo, aumentar e reduzir o volume)
    13. Scrollbar: barra de rolagem
    14. Text: permite o usuário digitar múltiplas linhas de texto
    15. Toplevel: um container, como um Frame, mas exibe sua própria janela

'''
import tkinter

class MinhaGUI:
    def __init__(self):
        #Criando a janela principal
        main_window = tkinter.Tk()

        #Exibindo a janela principal em looping
        tkinter.mainloop()

minha_gui = MinhaGUI()