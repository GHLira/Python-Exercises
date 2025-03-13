import math as m
# Obter a idade em anos, meses e dias, e informar a idade em dias
anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite o número de meses: "))
dias = int(input("Digite o número de dias: "))

# Calculando idade em dias
idade_em_dias = (anos * 365) + (meses * 30) + dias
print(f"Sua idade total em dias é: {idade_em_dias} dias")
