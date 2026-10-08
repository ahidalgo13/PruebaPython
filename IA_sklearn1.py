# 1. Importar librerías necesarias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 2. Crear nuestro propio dataset de animales
datos = {
    'peso':          [5000, 300, 80, 0.5, 2, 400, 0.03, 1.5, 60, 8, 25, 0.02, 700, 1.2, 4, 900, 0.05, 3, 15, 250, 0.1, 5, 1200, 0.8, 6, 30, 0.3, 2.5, 400, 0.6],
    'altura':        [320, 150, 120, 20, 30, 140, 15, 25, 90, 50, 60, 18, 200, 35, 45, 180, 20, 40, 70, 130, 25, 55, 250, 30, 65, 85, 22, 38, 160, 28],
    'tiene_pelo':    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'pone_huevos':   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'sangre_caliente':[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'num_patas':     [4, 4, 4, 4, 4, 4, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    'clase':         ['mamifero']*10 + ['ave']*10 + ['reptil']*10
}

# Mejor lo armamos bien por grupos:
datos = {
    'peso':           [5000, 300, 80, 70, 0.5, 2, 400, 1200, 60, 900],
    'altura':         [320, 150, 120, 170, 20, 30, 140, 250, 90, 180],
    'tiene_pelo':     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'pone_huevos':    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'sangre_caliente':[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'num_patas':      [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    'clase':          ['mamifero']*10
}

# Aves
aves = {
    'peso':           [2, 0.03, 1.5, 0.02, 1.2, 0.05, 3, 0.1, 0.8, 0.3],
    'altura':         [30, 15, 25, 18, 35, 20, 40, 25, 30, 22],
    'tiene_pelo':     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'pone_huevos':    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'sangre_caliente':[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'num_patas':      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    'clase':          ['ave']*10
}

# Reptiles
reptiles = {
    'peso':           [60, 8, 25, 700, 4, 15, 250, 5, 1200, 6],
    'altura':         [50, 60, 60, 200, 45, 70, 130, 55, 250, 65],
    'tiene_pelo':     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'pone_huevos':    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'sangre_caliente':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'num_patas':      [0, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    'clase':          ['reptil']*10
}

# Unimos todo
df = pd.concat([pd.DataFrame(datos), pd.DataFrame(aves), pd.DataFrame(reptiles)], ignore_index=True)

print("Total de animales:", len(df))
print("\nPrimeras filas:")
print(df.head())
print("\nDistribución de clases:")
print(df['clase'].value_counts())

# 3. Separar características (X) y etiquetas (y)
X = df.drop('clase', axis=1)
y = df['clase']

# 4. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 5. Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Crear y entrenar el modelo (Árbol de Decisión)
modelo = DecisionTreeClassifier(max_depth=4, random_state=42)
modelo.fit(X_train_scaled, y_train)

# 7. Predecir
y_pred = modelo.predict(X_test_scaled)

# 8. Evaluar
print(f"\nPrecisión: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))
print("Matriz de confusión:")
print(confusion_matrix(y_test, y_pred, labels=modelo.classes_))
print("Clases:", modelo.classes_)

# 9. Predecir animales nuevos
animales_nuevos = pd.DataFrame({
    'peso':           [1.5, 350, 20],
    'altura':         [25, 160, 55],
    'tiene_pelo':     [0, 1, 0],
    'pone_huevos':    [1, 0, 1],
    'sangre_caliente':[1, 1, 0],
    'num_patas':      [2, 4, 4]
})

animales_nuevos_scaled = scaler.transform(animales_nuevos)
predicciones = modelo.predict(animales_nuevos_scaled)

print("\n🐾 Predicciones de animales nuevos:")
for i, pred in enumerate(predicciones):
    print(f"  Animal {i+1}: {pred}")