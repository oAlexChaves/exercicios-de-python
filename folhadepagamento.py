
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