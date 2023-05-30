import csv

with open("endpoint.csv", mode='r') as file:
    reader = csv.reader(file, delimiter='\t')
    next(reader)  # Omitir la primera fila (cabecera)
    for row in reader:
        author = row[0]
        quote = row[1]
        print("Autor:", author)
        print("Cita:", quote)
        print()
