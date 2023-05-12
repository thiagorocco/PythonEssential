#os.path.basename - retorna o recurso de um path
#os.path.dirname - retorna todo o caminho até o recurso
#os.path.split() - retorna ambos separados em uma tupla 
import os
caminho = 'C:\\Estudo\\Python\\script.py'

print('Basename = ',os.path.basename(caminho))
print('Dirname = ',os.path.dirname(caminho))
print('Split = ',os.path.split(caminho))

''' Resultados:
    script.py
    C:\Estudo\Python
    ('C:\\Estudo\\Python','script.py')

'''