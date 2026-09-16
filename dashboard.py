import matplotlib.pyplot as plt

# Dados de exemplo - depois você troca pelos reais
dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]
toneladas = [1250, 1380, 1420, 1190, 1500, 980]

plt.figure(figsize=(8,5))
plt.bar(dias, toneladas, color="#2e7d32")
plt.title("Moagem Diária - Usina (toneladas)")
plt.xlabel("Dia")
plt.ylabel("Toneladas")
plt.grid(axis="y", alpha=0.3)

for i, v in enumerate(toneladas):
    plt.text(i, v+20, str(v), ha="center")

plt.tight_layout()
plt.savefig("moagem.png")
print("Gráfico salvo como moagem.png")

# Média
media = sum(toneladas) / len(toneladas)
print(f"Média semanal: {media:.0f} ton/dia")