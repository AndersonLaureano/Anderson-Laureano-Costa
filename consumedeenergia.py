try:
    # Entrada de dados
    aparelho = input("Digite o nome do aparelho: ")
    potencia = float(input(f"Digite a potência da(o) {aparelho} em Watts (W): "))
    horas_dia = float(input(f"Digite o tempo médio de uso diário (em horas): "))

    # Cálculo do consumo mensal (30 dias)
    consumo_mensal = (potencia * horas_dia * 30) / 1000

    # Saída de dados
    print("\n--- Resultado ---")
    print(f"Aparelho: {aparelho}")
    print(f"Consumo mensal: {consumo_mensal:.2f} kWh")

except ValueError:
    print("\nErro: Digite apenas valores numéricos para potência e horas.")