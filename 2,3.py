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

    with open("endpoint.csv", mode='w', newline='') as file:
        escritor = csv.writer(file, delimiter='\t')
        escritor.writerow(["author", "quote"])
        escritor.writerows(valores)

    print("Archivo CSV guardado exitosamente.")
else:
    print("Error al realizar la solicitud al endpoint.")