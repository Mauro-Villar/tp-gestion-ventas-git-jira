import pandas as pd
import matplotlib.pyplot as plt
import os

# Creamos la carpeta resultados por si no existe.
# Esto ayuda a que el script pueda ejecutarse sin problemas desde Colab.
os.makedirs("resultados", exist_ok=True)

# Leemos el dataset desde la carpeta datos.
# El parámetro sep=None intenta detectar automáticamente el separador del archivo.
df = pd.read_csv("datos/dataset.csv", sep=None, engine="python")

# Convertimos la fecha a formato fecha para poder trabajar por mes.
df["sales_date"] = pd.to_datetime(df["sales_date"])

# Calculamos las ventas totales.
ventas_totales = df["sales_amount"].sum()

# Calculamos el promedio de ventas.
venta_promedio = df["sales_amount"].mean()

# Buscamos el día con mayor venta.
dia_mayor_venta = df.loc[df["sales_amount"].idxmax()]

# Creamos una columna de mes para agrupar las ventas.
df["mes"] = df["sales_date"].dt.to_period("M")

# Calculamos las ventas por mes.
ventas_por_mes = df.groupby("mes")["sales_amount"].sum()

# Guardamos un resumen en la carpeta resultados.
with open("resultados/resumen_ventas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Resumen del análisis de ventas\n")
    archivo.write("--------------------------------\n")
    archivo.write(f"Ventas totales: {ventas_totales}\n")
    archivo.write(f"Venta promedio: {venta_promedio:.2f}\n")
    archivo.write(f"Día con mayor venta: {dia_mayor_venta['sales_date'].date()}\n")
    archivo.write(f"Monto de mayor venta: {dia_mayor_venta['sales_amount']}\n")
    archivo.write("\nVentas por mes:\n")
    archivo.write(str(ventas_por_mes))

# Generamos un gráfico simple de ventas por mes.
ventas_por_mes.plot(kind="bar", title="Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Monto de ventas")
plt.tight_layout()
plt.savefig("resultados/grafico_resultados.png")

print("Análisis finalizado correctamente.")
print("Los resultados se guardaron en la carpeta resultados.")
