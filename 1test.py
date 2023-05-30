import os
import datetime

# Obtener la hora actual
now = datetime.datetime.now()

# Obtener la hora de inicio de la última hora cerrada
last_closed_hour = now - datetime.timedelta(hours=1)
start_time = last_closed_hour.replace(minute=0, second=0, microsecond=0)

# Obtener la hora de fin del intervalo (hora actual redondeada hacia arriba)
if now.hour == 0:
    end_time = now.replace(hour=23, minute=59, second=59, microsecond=0)
else:
    end_time = now.replace(hour=now.hour-1, minute=59, second=59, microsecond=0)

# Obtener el día actual en formato 'May 29'
current_day = now.strftime('%b %d')

# Manejar el cambio de día
if last_closed_hour.day != now.day:
    current_day = last_closed_hour.strftime('%b %d') + ' - ' + now.strftime('%b %d')

# Abrir el archivo de registro
with open('/var/log/audit/audit.log', 'r') as archivo:
    # Inicializar contador de intentos fallidos
    failed_attempts_count = 0
    
    # Leer cada línea del archivo
    for linea in archivo:
        # Buscar las líneas que contienen "authentication" y están dentro del rango de tiempo
        if 'authentication' in linea and current_day in linea:
            timestamp = linea.split()[1]
            # Obtener la hora de la línea en formato 'HH:MM:SS'
            hora = datetime.datetime.strptime(timestamp, '%H:%M:%S').time()
            # Verificar si la hora está dentro del rango deseado
            if start_time.time() <= hora <= end_time.time():
                # Incrementar el contador de intentos fallidos
                failed_attempts_count += 1

# Mostrar el resultado sin segundos
print(f"Cantidad de intentos fallidos de inicio de sesión en el rango {current_day} {start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}: {failed_attempts_count}")
