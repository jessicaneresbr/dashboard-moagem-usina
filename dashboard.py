import csv
from datetime import datetime

print("=== DASHBOARD PRODUÇÃO - USINA ===")
print("1 - Registrar produção do dia")
print("2 - Ver total produzido")
op = input("Opção: ")

ARQUIVO = "producao.csv"

if op == "1":
    data = datetime.now().strftime("%d/%m/%Y")
    toneladas = input("Toneladas de cana moída: ")
    litros = input("Litros de álcool produzidos: ")
    with open(ARQUIVO, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([data, toneladas, litros])
    print("✓ Salvo!")

elif op == "2":
    try:
        total_ton = 0
        total_litros = 0
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for row in csv.reader(f):
                total_ton += float(row[1])
                total_litros += float(row[2])
        print(f"Total cana: {total_ton} ton")
        print(f"Total álcool: {total_litros} litros")
    except:
        print("Nenhum dado ainda.")