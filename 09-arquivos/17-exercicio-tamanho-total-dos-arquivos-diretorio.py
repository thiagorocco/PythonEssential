import os

os.system('cls') or None
tamanho = 0

for filename in os.listdir('C:\\Windows\\System32'):
    tamanho += os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print('Tamanho total da pasta System32',tamanho)