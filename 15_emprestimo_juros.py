import math as m
emprestimo = float(input("Digite o valor do empréstimo: "))
juros_simples = emprestimo * (1 + (0.008 * 12))
print(f"Valor final com juros simples: {juros_simples:.2f}")

juros_compostos = emprestimo * (1.008 ** 12)
print(f"Valor final com juros compostos: {juros_compostos:.2f}")
