import matplotlib.pyplot as plt

# Constantes físicas (mesmos valores do relatório em LaTeX)
k = 8.99e9   # N·m²/C²
q1 = 1.0    # 1 C
q2 = 1.0    # 1 C

# Distâncias de 0,10 m até 1,00 m (passo de 0,01 m)
distancias = [0.10 + i * 0.01 for i in range(91)]
energia = [k * q1 * q2 / r for r in distancias]

plt.figure(figsize=(6, 4))
plt.plot(distancias, energia, color="tab:blue", linewidth=2)
plt.title("Energia potencial vs. Distância")
plt.xlabel("Distância r (m)")
plt.ylabel("Energia U (J)")
plt.grid(True)
plt.tight_layout()
plt.savefig("energia_potencial.png", dpi=150)
print("Gráfico salvo em energia_potencial.png!")
