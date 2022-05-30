#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são #do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o #Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a #empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. #O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas #trabalhadas no mês.
#   Desconto do IR:
#   Salário Bruto até 900 (inclusive) - isento
#   Salário Bruto até 1500 (inclusive) - desconto de 5%
#   Salário Bruto até 2500 (inclusive) - desconto de 10%
#   Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,


valor_hora = float(input("quanto vale sua hora trabalhada? "))
horas_trabalhadas = float(input("Quantas horas você trabalhou este mês? "))

salario_bruto = (float(valor_hora * horas_trabalhadas))

if salario_bruto <= 900:
    desconto_ir = 0

elif salario_bruto <= 1500:
    desconto_ir = 5

elif salario_bruto <= 2500:
    desconto_ir = 10

else:
    desconto_ir = 20

ir = salario_bruto * (desconto_ir / 100)
sindicato = salario_bruto * (3 / 100)
fgts = salario_bruto * (11/ 100)
descontos = (ir + fgts)
salario_liquido = salario_bruto - (descontos)

print(
    "salario bruto:{:.2f} ".format(salario_bruto),
    "\n IR ({:.2f}%): {:.2f}".format(desconto_ir, ir),
    "\n sindicato (3%): {:.2f}".format(sindicato),
    "\n fgts (11%): {:.2f}".format(fgts),
    "\n total de descontos: {:.2f}".format(descontos),
    "\n70salario liquido: {:.2f}".format(salario_liquido)
)