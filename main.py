import sys
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Dataset proveniente del Servicio Sismológico Nacional
# Datos a partir de 1/1/1900 - 20/09/2022
# Todas las entidades federativas
# Magnitud 4.0 - 9.9
# Todas las profundidades

# Fecha,Hora,Magnitud,Latitud,Longitud,Profundidad,"Referencia de localizacion","Fecha UTC","Hora UTC","Estatus"

def most_repeated_magnitudes(dataset):
    common_magnitudes = dataset.Magnitud.value_counts()
    common_magnitudes.plot(kind="bar", grid=True)
    plt.title('Frecuencia de magnitudes 1900-2022')
    plt.xlabel("Magnitud")
    plt.ylabel("# Eventos con tal magnitud")
    plt.show()

def earhquakes_per_month(dataset):
    # Group by # of eq by month
    sortedSismos = dataset.sort_values(by=["Month"])

    # Not sure that this line works as I expect
    grouped_earthquakes = sortedSismos.groupby(sortedSismos.Month).size()

    grouped_earthquakes.plot(kind="bar", grid=True)
    plt.title('Número de sismos mensuales 1900-2022')
    plt.xlabel("Mes")
    plt.ylabel("# Sismos")
    plt.show()

def main():
    plt.close("all")

    sismos = pd.read_csv('dataset/SSNMX_catalogo_19000101_20220920_m40_99.csv')

    # Adding ID column
    sismos["ID"] = sismos.index

    # Adding month colum
    sismos["Fecha"] = pd.to_datetime(sismos.Fecha, format='%Y-%m-%d')
    sismos["Month"] = sismos["Fecha"].dt.month

    # General information about the data set
    sismos.info()

    # Run only ONE of the following until I figure out how to create multiple graphs without blocking the script execution ¯\_(ツ)_/¯
    most_repeated_magnitudes(sismos)
    # earhquakes_per_month(sismos)

if __name__ == '__main__':
    main()


