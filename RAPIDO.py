import pandas as pd
import time

print("1. Cargando base de datos gigante...")
# Supongamos que esto tarda 10 segundos en cargar
time.sleep(10) 
datos = pd.DataFrame({'ventas': [100, 200, 300], 'gastos': [50, 80, 120]})
print("2. Datos cargados con éxito")

# --- A PARTIR DE AQUÍ QUIERES PROBAR COSAS ---
ingresos_netos = datos['ventas'] - datos['gastos']
print(ingresos_netos)
promedio_ventas = datos['ventas'].mean()
print(promedio_ventas)