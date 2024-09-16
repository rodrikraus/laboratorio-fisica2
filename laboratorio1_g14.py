import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Extensión del gráfico
y_min, y_max = -2, 2
x_min, x_max = -2, 2

# Definición de las cargas y sus posiciones
cargas = [
    {'q': 1e-9, 'xq': 1, 'yq': 1},    # Carga positiva de 1 nC en (1, 1)
    {'q': -1e-9, 'xq': -1, 'yq': 1},  # Carga negativa de -1 nC en (-1, 1)
    {'q': 1e-9, 'xq': 0, 'yq': -1},   # Carga positiva de 1 nC en (0, -1)
    {'q': -1e-9, 'xq': 0, 'yq': 0},    # Carga positiva de -1 nC en (0, 0)
]

# Constantes
epsilon_0 = 8.854e-12  # Constante de permitividad eléctrica en el vacío (F/m)

# Función para calcular el campo eléctrico debido a una carga puntual
def campo_electrico(q, xq, yq, x, y):
    k = 1 / (4 * np.pi * epsilon_0)  # Constante de Coulomb    
    r = np.sqrt((x - xq)**2 + (y - yq)**2)
    Ex = (k * q * (x - xq)) / (r**3)
    Ey = (k * q * (y - yq)) / (r**3)
    return Ex, Ey

# Función para calcular el potencial eléctrico debido a una carga puntual
def potencial_electrico(q, xq, yq, x, y):
    k = 1 / (4 * np.pi * epsilon_0)  # Constante de Coulomb
    r = np.sqrt((x - xq)**2 + (y - yq)**2)
    V = k * q / r
    return V

# Creación de una malla de puntos en 2D
x = np.linspace(y_min, y_max, 100)
y = np.linspace(y_min, y_max, 100)
X, Y = np.meshgrid(x, y)

# Inicialización del campo eléctrico total (matrices)
Ex_total = np.zeros_like(X)
Ey_total = np.zeros_like(Y)

# Inicialización del potencial eléctrico total (matriz)
V_total = np.zeros_like(X)

# Cálculo del campo eléctrico total
for carga in cargas:
    Ex, Ey = campo_electrico(carga['q'], carga['xq'], carga['yq'], X, Y)
    Ex_total += Ex
    Ey_total += Ey

# Cálculo del potencial eléctrico total
for carga in cargas:
    V = potencial_electrico(carga['q'], carga['xq'], carga['yq'], X, Y)
    V_total += V

# Generación de gráficos
plot_base = plt.figure(figsize=(16, 8))
plot = plot_base.add_subplot(121)

# Generación de líneas de campo con librería Streamplot
color = 2 * np.log(np.hypot(Ex, Ey))
plot.streamplot(x, y, Ex_total, Ey_total, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=1.5, arrowstyle='->', arrowsize=1.5)

# Generación de un punto para cada carga en gráfico de líneas de campo
colores_carga = {True: '#aa0000', False: '#0000aa'}

for indice, carga in enumerate(cargas):
    pos = carga['xq'], carga['yq']
    ref = f"q{indice} = {carga['q']} en pos ({carga['xq']}, {carga['yq']})" # String para las referencias
    plot.add_artist(Circle(pos, 0.05, color=colores_carga[carga['q']>0], label=ref))

# Graficar gráfico: Lineas de campo
plot.set_title("Lineas de campo")
plot.set_xlabel('$x$')
plot.set_ylabel('$y$')
plot.set_xlim(y_min,y_max)
plot.set_ylim(y_min,y_max)
plot.set_aspect('equal')
plt.grid()
plt.legend(loc="upper left")

# Graficar gráfico: Potencial eléctrico
plt.subplot(122)
plt.contour(X, Y, V_total, 1200, cmap='viridis')
plt.title("Contorno del Potencial Eléctrico")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.colorbar(label="Potencial (V)")

plt.savefig('campo_y_potencial.png')