data = input(str("digite a data de seu nascimento no seguinte formato (dd/mm/aaaa): "))

dia, mes, ano = data.split('/')

if mes == ("01"):
    mesext = ("janeiro")
elif mes == ("02"):
    mesext = ("feveirero")
elif mes == ("03"):
    mesext = ("março")
elif mes == ("04"):
    mesext = ("abril")
elif mes == ("05"):
    mesext = ("maio")
elif mes == ("06"):
    mesext = ("junho")
elif mes == ("07"):
    mesext = ("julho")
elif mes == ("08"):
    mesext = ("agosto")
elif mes == ("09"):
    mesext = ("setembro")
elif mes == ("10"):
    mesext = ("outubro")
elif mes == ("11"):
    mesext = ("novembro")
elif mes == ("12"):
    mesext = ("dezembro")
else:
    ("refaça com uma data no formato estabelecido")
print("{} de {} de {}".format(dia, mesext, ano))