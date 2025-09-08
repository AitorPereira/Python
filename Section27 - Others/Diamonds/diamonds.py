import pandas as pd

# Ruta al archivo
file_path = "/Users/aitor/Downloads/anillos.xlsx"  # ajusta si fuese otra ruta

# Lee el Excel con openpyxl
df = pd.read_excel(file_path, sheet_name="Sheet1", engine="openpyxl")

# Asegura que las columnas existen (opcional pero útil)
esperadas = {"Precio", "Quilates"}
faltan = esperadas - set(df.columns)
if faltan:
    raise ValueError(f"Faltan columnas en el Excel: {faltan}")

# Limpieza de 'Precio' con formato europeo:
# - elimina punto de miles
# - cambia coma decimal por punto
# - convierte a número
df["Precio"] = (
    df["Precio"].astype(str)
    .str.replace(".", "", regex=False)   # quita separador de miles
    .str.replace(",", ".", regex=False)  # coma decimal -> punto
)
df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce")

# Asegura 'Quilates' numérico
df["Quilates"] = pd.to_numeric(df["Quilates"], errors="coerce")

# Filtra filas inválidas
df = df.dropna(subset=["Precio", "Quilates"])
df = df[df["Quilates"] > 0].copy()

# Calcula precio por quilate
df["Precio_por_Quilate"] = df["Precio"] / df["Quilates"]

# Top 10 más baratos y más caros por quilate
top10_baratos = df.sort_values("Precio_por_Quilate", ascending=True).head(10).copy()
top10_caros   = df.sort_values("Precio_por_Quilate", ascending=False).head(10).copy()

# Formato bonito para imprimir/guardar
def fmt(dfa):
    out = dfa[["Precio", "Quilates", "Precio_por_Quilate"]].copy()
    return out.round({"Precio": 2, "Quilates": 2, "Precio_por_Quilate": 2})

print("Top 10 más baratos por quilate:\n", fmt(top10_baratos).to_string(index=False))
print("\nTop 10 más caros por quilate:\n", fmt(top10_caros).to_string(index=False))

# Guarda ambos en un Excel nuevo con dos hojas
salida = "/Users/aitor/Documents/Python/Python/Diamonds/diamantes_top10.xlsx"
with pd.ExcelWriter(salida, engine="openpyxl") as writer:
    fmt(top10_baratos).to_excel(writer, sheet_name="Baratos_por_quilate", index=False)
    fmt(top10_caros).to_excel(writer, sheet_name="Caros_por_quilate", index=False)

print(f"\nResultados guardados en: {salida}")