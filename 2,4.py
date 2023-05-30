
import csv
from collections import Counter
import re

palabras_excluidas = ['the', 'a', 'an', 'and', 'or', 'but', 'for', 'with', 'in', 'on', 'at', 'to', 'from', 't','ve']  # Palabras a excluir en inglés

contador = Counter()  # Contador de palabras

with open("endpoint.csv", mode='r') as file:
    lector = csv.reader(file, delimiter='\t')
    next(lector)  # Omitir la primera fila (cabecera)
    for row in lector:
        cita = row[1]
        palabras = re.findall(r"\b(?:\w+(?:'\w+)?|\w+)\b", cita)  # Extraer palabras completas con apóstrofes

        # Incrementar el contador de palabras (excluyendo las palabras excluidas)
        for palabra in palabras:
            if palabra.lower() not in palabras_excluidas:
                contador[palabra.lower()] += 1

# Obtener las diez palabras más repetidas
top_ten = contador.most_common(10)

# Mostrar el ranking
print("Ranking de las diez palabras más repetidas:")
for i, (palabra, count) in enumerate(top_ten, start=1):
    print(f"{i}. Palabra: {palabra}, Repeticiones: {count}")

