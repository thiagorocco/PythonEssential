'''
9. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato 
e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 

O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% 
    
    Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    Salário Bruto: (5 * 220): R$ 1100,00
    (-) IR (5%)             : R$   55,00 
    (-) INSS ( 10%)         : R$  110,00
    FGTS (11%)              : R$  121,00
    Total de descontos      : R$  165,00
    Salário Liquido         : R$  935,00
'''
valorHora = float(input('Informe o valor da sua hora de trabalho: '))
horasTrabalhadas = float(input('Informe quantas horas você trabalhou: '))
salarioBruto = valorHora * horasTrabalhadas
perc_fgts = 11
fgts = salarioBruto * perc_fgts/100
perc_sindicato = 3
sindicato = salarioBruto * perc_sindicato/100
perc_inss = 10
inss = salarioBruto * perc_inss/100

if salarioBruto <= 900.00:
    perc_ir = 0
elif salarioBruto > 900.00 and salarioBruto <= 1500.00:
    perc_ir = 5
elif salarioBruto > 1500.00 and salarioBruto <= 2500.00:
    perc_ir = 10
elif salarioBruto > 2500:
    perc_ir = 20

ir = salarioBruto * perc_ir/100
descontos = sindicato + inss + ir
salarioLiquido = salarioBruto - descontos

print('Salário Bruto:\t\t%.2f' %salarioBruto)
print('IR:(%.2f):\t\t%.2f' %(perc_ir,ir))
print('INSS(%.2f):\t\t%.2f' %(perc_inss,inss))
print('Sindicato(%.2f):\t%.2f' %(perc_sindicato,sindicato))
print('FGTS(%.2f):\t\t%.2f' %(perc_fgts,fgts))
print('Total descontos:\t%.2f' %descontos)
print('Salário Líquido:\t%.2f' %salarioLiquido)