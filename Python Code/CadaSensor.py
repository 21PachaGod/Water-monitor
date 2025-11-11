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

# Criar função para gerar gráfico de linhas de um sensor
def plot_sensor(sensor_data, sensor_name, filename):
    plt.figure(figsize=(10, 6))
    plt.plot(sensor_data, label=sensor_name, marker="o", color="b")
    plt.title(f"Temperaturas Registradas - {sensor_name}", fontsize=14)
    plt.xlabel("Tempo (amostras)", fontsize=12)
    plt.ylabel("Temperatura (°C)", fontsize=12)
    plt.grid()
    plt.legend()
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.show()

# Gerar gráficos para cada sensor
plot_sensor(sensor1_temperatures, "Sensor 1", "sensor1_temperaturas.png")
plot_sensor(sensor2_temperatures, "Sensor 2", "sensor2_temperaturas.png")
plot_sensor(sensor3_temperatures, "Sensor 3", "sensor3_temperaturas.png")
