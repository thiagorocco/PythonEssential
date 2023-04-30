def conta_caractere(texto, char):
    count = 0
    for letra in texto:
        if letra == char:
            count += 1
    print(char,' apareceu ',count,' vezes na string')

string = input('Digite um texto qualquer: ')
caractere = input('Digite um caractere: ')

conta_caractere(string, caractere)