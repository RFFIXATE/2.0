import csv

with open("endpoint.csv", mode='r') as archivo:
    lector = csv.reader(archivo, delimiter='\t')
    next(lector)  # Omitir la primera fila (cabecera)
    for row in lector:
        author = row[0]
        quote = row[1]
        print("Autor:", author)
        print("Cita:", quote)
        print()
