PI = 3.14

def perimetro(raio):
    print("Perimetro: ", 2*PI*raio)

def area(raio):
    print("Área: ", PI*raio*raio)

raio = float(input("Raio do círculo: "))
perimetro(raio)
area(raio)

#Apesar da recomendação de constantes em maiúscula com underline: ex: LOCAL_HOST 
#O valor ainda poderá ser incrementado/decrementado ou mesmo alterado.
#PI +=1
#print(PI)