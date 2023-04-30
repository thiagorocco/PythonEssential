'''
6. Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
num1 = float(input('Informe o primeiro número: ')) 
num2 = float(input('Informe o segundo número: ')) 
num3 = float(input('Informe o terceiro número: ')) 

if num1 > num2 and num1 > num3 and num2 > num3:
    print(num1,'\n',num2,'\n',num3)
elif num2 > num3 and num1 > num3:
    print(num2,'\n',num1,'\n',num3)
elif num2 > num3 and num1 < num3:
    print(num2,'\n',num3,'\n',num1)
elif num2 > num1:
    print(num3,'\n',num2,'\n',num1)
elif num1 > num2:
    print(num3,'\n',num1,'\n',num2)

    