from associacaoClasses import Escritor
from associacaoClasses import Caneta
from associacaoClasses import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

