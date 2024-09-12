import numpy as np
import matplotlib.pyplot as plt

# Constantes
epsilon_0 = 8.854e-12  # Constante de permitividad eléctrica en el vacío (F/m)

# Función para calcular el campo eléctrico debido a una carga puntual
def campo_electrico(q, xq, yq, x, y):
    k = 1 / (4 * np.pi * epsilon_0)  # Constante de Coulomb
    r = np.sqrt((x - xq)**2 + (y - yq)**2)
    Ex = k * q * (x - xq) / r**3
    Ey = k * q * (y - yq) / r**3
    return Ex, Ey

# Función para calcular el potencial eléctrico debido a una carga puntual
def potencial_electrico(q, xq, yq, x, y):
    k = 1 / (4 * np.pi * epsilon_0)  # Constante de Coulomb
    r = np.sqrt((x - xq)**2 + (y - yq)**2)
    V = k * q / r
    return V

# Definir las cargas y sus posiciones
cargas = [
    {'q': 1e-9, 'xq': 1, 'yq': 1},    # Carga positiva de 1 nC en (1, 1)
    {'q': -1e-9, 'xq': -1, 'yq': 1},  # Carga negativa de -1 nC en (-1, 1)
    {'q': 1e-9, 'xq': 0, 'yq': -1}    # Carga positiva de 1 nC en (0, -1)
]

# Crear una malla de puntos en 2D
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Inicializar el campo eléctrico total
Ex_total = np.zeros_like(X)
Ey_total = np.zeros_like(Y)

# Calcular el campo eléctrico total
for carga in cargas:
    Ex, Ey = campo_electrico(carga['q'], carga['xq'], carga['yq'], X, Y)
    Ex_total += Ex
    Ey_total += Ey

# Graficar las líneas de campo eléctrico
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, Ex_total, Ey_total, color='b')
plt.title("Líneas de Campo Eléctrico")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig('lineas_campo.png')

# Inicializar el potencial eléctrico total
V_total = np.zeros_like(X)

# Calcular el potencial eléctrico total
for carga in cargas:
    V = potencial_electrico(carga['q'], carga['xq'], carga['yq'], X, Y)
    V_total += V

# Graficar el contorno del potencial eléctrico
plt.figure(figsize=(8, 8))
plt.contour(X, Y, V_total, 50, cmap='viridis')
plt.title("Contorno del Potencial Eléctrico")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.colorbar(label="Potencial (V)")
plt.savefig('potencial.png')

# Graficar el campo y el potencial eléctrico en un solo gráfico
plt.figure(figsize=(10, 10))
plt.quiver(X, Y, Ex_total, Ey_total, color='b')
plt.contour(X, Y, V_total, 50, cmap='viridis')
plt.title("Campo y Potencial Eléctrico")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.colorbar(label="Potencial (V)")
plt.savefig('campo_potencial.png')
