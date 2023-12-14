def media(mat,fis,qui):
    media = (mat+fis+qui)/3
    print("Media: %.1f" %media)


media(8.0,7,10)
#Não importa a ordem se você usar argumentos nomeados!
media(qui=10,mat=8.0,fis=7)

#Porém atenção!
''' Mas existe uma importante regra que deve ser obedecida:
        
        Argumentos posicionais devem vir antes
        Os argumentos que não são nomeados, são automaticamente chaveados 
        de maneira sequencial, posicional, com a ordem dos parâmetros.
'''