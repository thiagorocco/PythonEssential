from associacaoClasses import Escritor
from associacaoClasses import Caneta
from associacaoClasses import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever()

#Esse tipo de associação também é conhecida como "associação fraca" ou "indireta"
#A associação forte seria referenciar de forma direta; EX: lista = [1,2,3]
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
try:
    escritor.ferramenta.escrever()
except:
    print('Objeto escritor foi removido. Não pode usar o método escrever associado.')

caneta.escrever()
maquina.escrever()

