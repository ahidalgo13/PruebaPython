import pandas as pd

datos = {'Producto': ['Manzana', 'Pera', 'Uva'], 'Precio': [1.5, 2.0, 3.5]}
df = pd.DataFrame(datos)
print(df)
print("Total:", df['Precio'].sum())