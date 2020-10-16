usd = input("¿Cuantos dolares tienes?: ")
usd = float(usd)
valor_dolar = 3875
pesos = usd * valor_dolar
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos")