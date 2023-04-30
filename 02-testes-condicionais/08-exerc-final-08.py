'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contrataram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
'''
salarioAtual = float(input('Informe o seu salário: '))
reajuste = 0
salarioFinal = 0

if salarioAtual < 280:
    reajuste = 20.0
elif salarioAtual >= 280.00 and salarioAtual < 700.00:
    reajuste = 15.0
elif salarioAtual >= 700.00 and salarioAtual  < 1500.00:
    reajuste = 10.0
elif salarioAtual >= 1500.00:
    reajuste = 5.0

salarioFinal = salarioAtual*(1+reajuste/100)

print('Salário antes do reajuste: %.2f' %salarioAtual)
print('Percentual do reajuste: ',reajuste,'%.')
print('Salário após o reajuste: %.2f' %salarioFinal)
