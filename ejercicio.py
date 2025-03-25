import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel('C:/Users/Alumno/Documents/Ejercicios/proyecto1.xlsx')

sumatoria_columna = df["ventas_tot"].sum()
print('Ventas totales:', sumatoria_columna)

desv_pagos = df["pagos_tot"].std()
print('Desviacion de los pagos', desv_pagos)

adeudo = df["adeudo_actual"].sum()
print('El adeudo total es:', adeudo)

Utilidad= ((df['ventas_tot'] - df['adeudo_actual']) / df['ventas_tot']) * 100
Utilidad1 = Utilidad.round(2)

print(Utilidad, ' La utilidad')

adeudo_si = df[df['B_adeudo'] == 'Con adeudo'].shape[0]  # Número de socios con adeudo
adeudo_no = df[df['B_adeudo'] == 'Sin adeudo'].shape[0]  # Número de socios sin adeudo

# Total de socios
total_socios = df.shape[0]

porcentaje_adeudo_si = (adeudo_si / total_socios) * 100
porcentaje_adeudo_no = (adeudo_no / total_socios) * 100

print(f"Socios con adeudo: {adeudo_si} ({porcentaje_adeudo_si:.2f}%)")
print(f"Socios sin adeudo: {adeudo_no} ({porcentaje_adeudo_no:.2f}%)")

df['fec_ini_cdto'] = pd.to_datetime(df['fec_ini_cdto'])

ventas_por_tiempo = df.groupby(df['fec_ini_cdto'].dt.to_period('M'))['ventas_tot'].sum()

plt.figure(figsize=(10, 6))
ventas_por_tiempo.plot(kind='bar')
plt.title('Ventas Totales por Mes')
plt.xlabel('Mes')
plt.ylabel('Ventas Totales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df['fec_ini_cdto'] = pd.to_datetime(df['fec_ini_cdto'])
desviacion_estandar = df.groupby(df['fec_ini_cdto'].dt.to_period('M'))['pagos_tot'].std()

plt.figure(figsize=(10, 6))
desviacion_estandar.plot(kind='bar')

plt.title('Desviación Estándar de los Pagos Realizados por Mes')
plt.xlabel('Mes')
plt.ylabel('Desviación Estándar')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()