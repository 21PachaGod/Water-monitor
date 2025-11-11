import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dados dos sensores
sensor1_temperatures = [
    12.00, 12.00, 12.00, 12.00, 12.00, 11.50, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00,
    12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00, 12.00,
    17.50, 17.50, 17.50, 17.50, 16.50, 16.00, 15.50, 15.00, 14.50, 14.00, 13.50, 13.00, 12.50, 12.00, 12.00, 12.00
]
sensor2_temperatures = [
    11.63, 11.69, 11.63, 11.69, 11.69, 11.63, 11.69, 11.63, 11.63, 11.69, 11.63, 11.69, 11.63, 11.69, 11.63, 11.69,
    11.75, 11.75, 11.69, 11.75, 11.75, 11.69, 11.75, 11.75, 11.75, 11.69, 11.75, 11.75, 11.69, 11.69, 11.75, 11.75
]
sensor3_temperatures = [
    11.50, 11.50, 11.50, 11.50, 11.50, 11.56, 11.50, 11.50, 11.50, 11.50, 11.50, 11.50, 11.50, 11.50, 11.50, 11.50,
    13.44, 13.38, 13.31, 13.25, 13.19, 13.13, 13.06, 13.00, 12.94, 12.88, 12.81, 12.75, 12.69, 12.63, 12.56, 12.50
]

# Preencher listas de tamanhos diferentes com NaN
max_length = max(len(sensor1_temperatures), len(sensor2_temperatures), len(sensor3_temperatures))
sensor1_temperatures += [np.nan] * (max_length - len(sensor1_temperatures))
sensor2_temperatures += [np.nan] * (max_length - len(sensor2_temperatures))
sensor3_temperatures += [np.nan] * (max_length - len(sensor3_temperatures))

# Criar DataFrame com os dados dos sensores
sensor_data = {
    "Sensor 1": sensor1_temperatures,
    "Sensor 2": sensor2_temperatures,
    "Sensor 3": sensor3_temperatures
}
df = pd.DataFrame(sensor_data)

# Criar gráfico de boxplot
plt.figure(figsize=(8, 6))
df.boxplot(column=["Sensor 1", "Sensor 2", "Sensor 3"], grid=False)

# Adicionar título e legendas
plt.title("Distribuição das Temperaturas por Sensor", fontsize=14)
plt.ylabel("Temperatura (°C)", fontsize=12)

# Salvar gráfico como PNG
plt.savefig("boxplot_temperaturas_sensores.png", dpi=300, bbox_inches="tight")
plt.show()
