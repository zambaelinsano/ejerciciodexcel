import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel('../ejerciciodexcel/proyecto1.xlsx')

sumatoria_columna = df["ventas_tot"].sum()
print('Ventas totales:', sumatoria_columna)

desv_pagos = df["pagos_tot"].std()
print('Desviacion de los pagos', desv_pagos)

adeudo = df["adeudo_actual"].sum()
print('El adeudo total es:', adeudo)

adeudo_si = df[df['B_adeudo'] == 'Con adeudo'].shape[0]  # Número de socios con adeudo
adeudo_no = df[df['B_adeudo'] == 'Sin adeudo'].shape[0]  # Número de socios sin adeudo

# Total de socios
total_socios = df.shape[0]

porcentaje_adeudo_si = (adeudo_si / total_socios) * 100
porcentaje_adeudo_no = (adeudo_no / total_socios) * 100

print(f"Socios con adeudo: {adeudo_si} ({porcentaje_adeudo_si:.2f}%)")
print(f"Socios sin adeudo: {adeudo_no} ({porcentaje_adeudo_no:.2f}%)")


ventas_por_tiempo = df.groupby(df['B_mes'].dt.to_period('M'))['ventas_tot'].sum()

plt.figure(figsize=(10, 6))
ventas_por_tiempo.plot(kind='bar')
plt.title('Ventas Totales por Mes')
plt.xlabel('Mes')
plt.ylabel('Ventas Totales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

desviacion_estandar = df.groupby(df['B_mes'].dt.to_period('M'))['pagos_tot'].std()

plt.figure(figsize=(10, 6))
desviacion_estandar.plot(kind='bar')

plt.title('Desviación Estándar de los Pagos Realizados por Mes')
plt.xlabel('Mes')
plt.ylabel('Desviación Estándar')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
porcentaje_utilidad = ((sumatoria_columna - adeudo) / sumatoria_columna) * 100


ventassucursal = df.groupby("id_sucursal")["ventas_tot"].sum()


plt.figure(figsize=(8, 8))
plt.pie(ventassucursal, labels=ventassucursal.index, autopct="%1.1f%%", startangle=140)
plt.title("Distribución de Ventas por Sucursal")
plt.show()

# 8. Gráfico de deudas totales por sucursal respecto del margen de utilidad
deudassucursal = df.groupby("id_sucursal")["adeudo_actual"].sum()
margenutil = (ventassucursal - deudassucursal) / ventassucursal * 100

fig, tabl = plt.subplots(figsize=(10, 5))

tabl.bar(deudassucursal.index, deudassucursal, color="#0f2b48", label="Deuda Total")
tabl.set_xlabel("Sucursales")
tabl.set_ylabel("Deuda Total", color="#0f2b48")
tabl.tick_params(axis="y", labelcolor="#0f2b48")

tabl2 = tabl.twinx()
tabl2.plot(margenutil.index, margenutil, marker="o", linestyle="--", color="#38b6ff", label="Margen de Utilidad")
tabl2.set_ylabel("Margen de Utilidad", color="red")
tabl2.tick_params(axis="y", labelcolor="blue")

plt.title("Deuda Total por Sucursal vs Margen de Utilidad")
fig.tight_layout()
plt.show()