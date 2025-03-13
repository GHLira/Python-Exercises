import math as m
hora_inicio, minuto_inicio = map(int, input("Hora e minuto de início (hh mm): ").split())
hora_fim, minuto_fim = map(int, input("Hora e minuto do fim (hh mm): ").split())
inicio = hora_inicio * 60 + minuto_inicio
fim = hora_fim * 60 + minuto_fim
duracao = fim - inicio

if duracao < 0:
    duracao += 1440  # Caso a partida vá para o dia seguinte

print(f"Duração: {duracao // 60} horas e {duracao % 60} minutos")

