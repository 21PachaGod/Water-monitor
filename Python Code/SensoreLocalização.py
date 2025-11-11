import pandas as pd
import matplotlib.pyplot as plt

# Dados do GPS
gps_data = {
    "Latitude": [
        37.638234, 37.638234, 37.638207, 37.638233, 37.638269, 37.638188, 37.638188, 37.638129, 37.638126, 37.638153,
        37.638153, 37.638148, 37.638147, 37.638148, 37.638138, 37.638138, 37.638138, 37.638133, 37.638126, 37.638115
        # Inclua mais linhas do conjunto de dados completo
    ],
    "Longitude": [
        -7.661751, -7.661751, -7.661751, -7.661732, -7.661737, -7.661749, -7.661749, -7.661751, -7.661747, -7.661737,
        -7.661737, -7.661731, -7.661735, -7.661748, -7.661698, -7.661698, -7.661733, -7.661738, -7.661744, -7.661749
        # Inclua mais linhas do conjunto de dados completo
    ],
    "Altitude": [
        0.00, -5.70, -5.70, 0.10, 0.10, 0.10, 1.80, 1.80, 11.60, 11.60, 6.30, 6.30, 6.30, 5.10, 5.10, 6.50, 6.50, 9.90, 9.90, 11.40
        # Inclua mais linhas do conjunto de dados completo
    ]
}

# Temperaturas dos sensores (use um subconjunto dos dados correspondentes ao GPS)
sensor1_temperatures = [
    12.00, 11.50, 12.00, 12.50, 13.00, 14.50, 15.00, 16.00, 17.50, 17.50, 17.50, 17.50, 16.50, 16.00, 15.50, 15.00, 14.50, 14.00, 13.50, 13.00
]
sensor2_temperatures = [
    11.63, 11.69, 11.75, 11.63, 11.69, 11.75, 11.63, 11.69, 11.75, 11.69, 11.75, 11.75, 11.69, 11.75, 11.75, 11.75, 11.69, 11.75, 11.75, 11.69
]
sensor3_temperatures = [
    11.50, 11.50, 11.50, 11.50, 11.50, 11.56, 11.50, 11.50, 11.50, 13.44, 13.38, 13.31, 13.25, 13.19, 13.13, 13.06, 13.00, 12.94, 12.88, 12.81
]

# Criar DataFrame
gps_df = pd.DataFrame(gps_data)
gps_df["Sensor 1"] = sensor1_temperatures
gps_df["Sensor 2"] = sensor2_temperatures
gps_df["Sensor 3"] = sensor3_temperatures

# Plotar gráficos de dispersão para cada sensor
for sensor in ["Sensor 1", "Sensor 2", "Sensor 3"]:
    plt.figure(figsize=(10, 6))
    sc = plt.scatter(
        gps_df["Longitude"], gps_df["Latitude"], c=gps_df[sensor], cmap="viridis", s=50, edgecolor="k"
    )
    plt.colorbar(sc, label=f"Temperatura ({sensor})")
    plt.title(f"Distribuição das Temperaturas - {sensor}", fontsize=14)
    plt.xlabel("Longitude", fontsize=12)
    plt.ylabel("Latitude", fontsize=12)
    plt.grid(True)
    plt.savefig(f"distribuicao_temperaturas_{sensor.lower().replace(' ', '_')}.png", dpi=300, bbox_inches="tight")
    plt.show()
