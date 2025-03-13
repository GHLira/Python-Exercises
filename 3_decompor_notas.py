import math as m

valor = int(input("Digite um valor para decompor em notas: "))
notas = [200, 100, 50, 20, 10, 5, 2]
quantidade_notas = {}

for nota in notas:
    quantidade_notas[nota] = valor // nota
    valor %= nota

print("Menor quantidade de notas:")
for nota, qtd in quantidade_notas.items():
    if qtd > 0:
        print(f"{qtd} nota(s) de {nota}")

