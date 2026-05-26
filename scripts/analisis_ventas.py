import pandas as pd
import matplotlib.pyplot as plt

# 1. Importar el archivo de ventas usando ruta relativa
try:
    df = pd.read_csv('../datos/ventas.csv')
    print("Datos cargados correctamente.\n")
except FileNotFoundError:
    print("Error: No se encontró el archivo. Verifique la carpeta /datos.")

# 2. Preparar los datos temporales
# Convertimos sales_date a formato fecha para poder extraer el mes
df['sales_date'] = pd.to_datetime(df['sales_date'])
df['mes'] = df['sales_date'].dt.month

# 3. Calcular indicadores
ventas_totales = df['sales_amount'].sum()
ventas_por_mes = df.groupby('mes')['sales_amount'].sum()

# NOTA TÉCNICA: El dataset 10.3 sugerido en el TP no incluye información de productos.
# Por lo tanto, se omite el indicador de "producto más vendido" para mantener la integridad de los datos provistos.

print(f"--- INDICADORES DE VENTAS ---")
print(f"Ventas Totales: ${ventas_totales}")
print("\nVentas Totales por Mes:")
print(ventas_por_mes.to_string())

# 4. Generar gráfico que represente la evolución de ventas
plt.figure(figsize=(10,5))
# Agrupamos por fecha exacta para ver la evolución diaria
evolucion_diaria = df.groupby('sales_date')['sales_amount'].sum()
evolucion_diaria.plot(kind='line', color='blue', marker='o')

plt.title('Evolución de Ventas (Escenario B)')
plt.xlabel('Fecha de Venta')
plt.ylabel('Monto Vendido ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# 5. Guardar el gráfico en la carpeta de resultados
plt.savefig('../resultados/evolucion_ventas.png')
print("\nGráfico evolutivo guardado exitosamente en /resultados/evolucion_ventas.png")
