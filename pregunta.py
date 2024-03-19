"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""

import pandas as pd


def ingest_data():

    with open("clusters_report.txt", "r") as file:
        data = file.readlines()
    data = [linea.strip() for linea in data]
    data = [linea.split() for linea in data]
    header = data[0]
    header = [
        header[0],
        " ".join(header[1:3]) + " " + " ".join(data[1][0:2]),
        " ".join(header[3:5]) + " " + " ".join(data[1][2:4]),
        " ".join(header[5:]),
    ]
    header = [colum.lower().replace(" ", "_") for colum in header]
    data = [linea for linea in data if len(linea) > 0]  # linea es una lista de la lista
    filas = []
    texto = ""
    lista2 = []
    for linea in data:
        if linea[0].isnumeric():
            if len(lista2) > 0:
                lista2 = lista2 + [texto]
                filas.append(lista2)
            lista2 = []
            texto = ""
            lista2 = linea[:3]
            texto = " ".join(linea[4:])
        else:
            texto = texto + " " + " ".join(linea)
    lista2 = lista2 + [texto]
    filas.append(lista2)
    print(header)
    df = pd.DataFrame(filas, columns=header)
    df["cluster"] = df["cluster"].astype(int)
    df["cantidad_de_palabras_clave"] = df["cantidad_de_palabras_clave"].astype(int)
    df["porcentaje_de_palabras_clave"] = (
        df["porcentaje_de_palabras_clave"].str.replace(",", ".").astype(float)
    )
    df["principales_palabras_clave"] = df["principales_palabras_clave"].str.replace(
        ".", ""
    )
    print(df.iloc[0, 3])

    # Inserte su código aquí
    #

    return df


print(ingest_data())
