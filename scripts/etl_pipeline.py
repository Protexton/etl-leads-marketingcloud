import pandas as pd

# Cargar datos
df = pd.read_csv("data/leads.csv")

# Limpiar y transformar
df["email"] = df["email"].str.lower()
df["high_score"] = df["score"] >= 70

# Mostrar segmentación
print("Leads con alta puntuación:")
print(df[df["high_score"] == True])
