'''
Uma pasta do Windows: C:\Windows\Jose\Python
Um diretório no Linux : /home/user/Maria/Python
Ou seja, as barras são invertidas!

Se tentar acessar um endereço que não existe
(como um C: no Linux ou /home no Windows) vai dar erro sim em seus scripts!

Por isso use os.path.join('string1','string2','string3')
'''
import os

print(os.path.join('home','user','Maria'))
#Se estiver no Windows, a função retorna a string: 'home\\user\\Maria'
#Se estiver no Linux, retorna a string: 'home//user//Maria'

