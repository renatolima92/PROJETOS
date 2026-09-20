# ⚡CALCULADORA CONSUMO ELÉTRICO⚡

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (em Watts): "))
tempo_de_uso_diário = float(input("Digite o tempo de uso diário (em horas): ")) 
consumo_mensal = (potencia * tempo_de_uso_diário * 30) / 1000  # Consumo mensal em kWh
custo_kwh = 0.75
custo_mensal = consumo_mensal * custo_kwh  # Custo mensal em R$
print(f"O consumo mensal do {aparelho} é de {consumo_mensal:.2f} kWh.")
print(f"O custo mensal do {aparelho} é de R$ {custo_mensal:.2f}.")
