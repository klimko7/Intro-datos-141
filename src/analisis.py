import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ruta_archivo = "data/usu_individual_T226.txt"

print("Leyendo la base de datos de la EPH...")

df = pd.read_csv(ruta_archivo, sep=";", encoding="latin-1")

print(f"Filas totales en el trimestre: {df.shape[0]}")

aglomerados_objetivo = [1, 2, 19]
df_filtrado = df[df["AGLOMERADO"].isin(aglomerados_objetivo)]

print(f"Filas filtradas (GBA y Córdoba): {df_filtrado.shape[0]}")

print("\nRegistros por aglomerado:")
print(df_filtrado["AGLOMERADO"].value_counts())