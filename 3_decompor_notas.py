import math as m

# Obter um valor e informar a menor quantidade possível de notas
valor = int(input("Digite um valor em reais: "))
notas_200 = valor // 200
valor %= 200
notas_100 = valor // 100
valor %= 100
notas_50 = valor // 50
valor %= 50
notas_20 = valor // 20
valor %= 20
notas_10 = valor // 10
valor %= 10
notas_5 = valor // 5
valor %= 5
notas_2 = valor // 2
valor %= 2

print(f"Notas de 200: {notas_200}")
print(f"Notas de 100: {notas_100}")
print(f"Notas de 50: {notas_50}")
print(f"Notas de 20: {notas_20}")
print(f"Notas de 10: {notas_10}")
print(f"Notas de 5: {notas_5}")
print(f"Notas de 2: {notas_2}")
