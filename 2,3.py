# pip install requests pandas
# para actualizar python.exe -m pip install --upgrade pip
# pip3 install requests

import requests
import csv

lectura = requests.get("https://dummyjson.com/quotes")
if lectura.status_code == 200:
    data = lectura.json()
    cita = data['quotes']
    valores = [[quote['author'], quote['quote']] for quote in cita]

    with open("endpoint.csv", mode='w', newline='') as archivo:
        escritor = csv.writer(archivo, delimiter='\t')
        escritor.writerow(["autor", "cita"])
        escritor.writerows(valores)

    print("Archivo CSV guardado exitosamente.")
else:
    print("Error al realizar la solicitud al endpoint.")