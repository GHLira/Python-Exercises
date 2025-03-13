import math as m
# Obter um valor de tempo dado em segundos e informar a conversão
segundos = int(input("Digite o valor em segundos: "))

dias = segundos // 86400
segundos %= 86400
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos")
