'''
    Use 2 underlines antes do atributo. Ex: __senha
'''
class Funcionario:
    def __init__(self):
        self.__senha = 'senha'
  
gerente = Funcionario()
print("Senha do gerente:", gerente.__senha)