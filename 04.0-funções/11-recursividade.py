def somatorio(x):
    if x==1:
        return 1
    else:
        return x + somatorio(x-1)
#a função vai chamando ela mesma e, sempre decrementando 01 até que seja igual a 1 e pare


x = int(input("Somatorio de 1 até: "))
print("Soma: ",somatorio(x) )