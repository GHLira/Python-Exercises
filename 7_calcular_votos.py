import math as m
# Obter os votos e calcular porcentagem de votos válidos, brancos e nulos
total_eleitores = int(input("Digite o número total de eleitores: "))
votos_brancos = int(input("Digite o número de votos brancos: "))
votos_nulos = int(input("Digite o número de votos nulos: "))
votos_validos = total_eleitores - votos_brancos - votos_nulos

porcentagem_validos = (votos_validos / total_eleitores) * 100
porcentagem_brancos_nulos = ((votos_brancos + votos_nulos) / total_eleitores) * 100

print(f"Porcentagem de votos válidos: {porcentagem_validos:.2f}%")
print(f"Porcentagem de votos brancos e nulos: {porcentagem_brancos_nulos:.2f}%")
